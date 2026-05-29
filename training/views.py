"""
Views for the training application.

The views include listings of techniques, detailed pages for techniques and
labs, and interactive quiz pages that display questions and calculate
results. Class-based views are used where appropriate to keep the code
concise and familiar to Django users.
"""

from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import ListView, DetailView
from django.urls import reverse

from .models import Technique, Quiz, Lab, Question
from .forms import QuizForm


class TechniqueListView(ListView):
    """Display a list of available MITRE ATT&CK techniques."""

    model = Technique
    template_name = 'training/technique_list.html'
    context_object_name = 'techniques'


class TechniqueDetailView(DetailView):
    """Show the details of a technique, including quizzes and labs."""

    model = Technique
    template_name = 'training/technique_detail.html'
    context_object_name = 'technique'


class LabDetailView(DetailView):
    """Display details of a lab exercise."""

    model = Lab
    template_name = 'training/lab_detail.html'
    context_object_name = 'lab'


def quiz_view(request, pk: int):
    """
    Present a quiz to the user and handle submission.

    When accessed via GET, this view displays the quiz questions. When the
    form is submitted via POST, it calculates the user's score based on
    correct choices and redirects to the results page.
    """
    quiz = get_object_or_404(Quiz, pk=pk)
    questions = quiz.questions.all()
    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = 0
            total = questions.count()
            user_answers = {}
            for question in questions:
                field_name = f'question_{question.id}'
                selected_choice = form.cleaned_data.get(field_name)
                user_answers[question.id] = selected_choice.id if selected_choice else None
                if selected_choice and selected_choice.is_correct:
                    score += 1
            # Store results in session for retrieval in the results view
            request.session['quiz_results'] = {
                'quiz_id': quiz.id,
                'score': score,
                'total': total,
                'user_answers': user_answers,
            }
            return redirect('training:quiz_results', pk=quiz.id)
    else:
        form = QuizForm(questions=questions)
    return render(request, 'training/quiz.html', {'quiz': quiz, 'form': form})


def quiz_result_view(request, pk: int):
    """
    Display the results of a completed quiz.

    The view retrieves the stored score and user answers from the session,
    matches them with the correct answers, and shows the user which
    questions were answered correctly or incorrectly.
    """
    quiz = get_object_or_404(Quiz, pk=pk)
    results = request.session.get('quiz_results')
    if not results or results.get('quiz_id') != quiz.id:
        # If there are no results, redirect to the quiz page
        return redirect('training:quiz', pk=quiz.id)
    score = results['score']
    total = results['total']
    user_answers = results['user_answers']
    detailed_results = []
    for question in quiz.questions.all():
        selected_choice_id = user_answers.get(question.id)
        selected_choice = None
        if selected_choice_id is not None:
            selected_choice = question.choices.get(id=selected_choice_id)
        correct_choice = question.choices.filter(is_correct=True).first()
        detailed_results.append({
            'question': question,
            'selected': selected_choice,
            'correct': correct_choice,
            'is_correct': selected_choice == correct_choice,
        })
    # Remove results from session to avoid showing stale data
    del request.session['quiz_results']
    return render(
        request,
        'training/quiz_results.html',
        {
            'quiz': quiz,
            'score': score,
            'total': total,
            'detailed_results': detailed_results,
        },
    )