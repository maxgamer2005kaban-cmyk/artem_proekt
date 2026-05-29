"""
Forms for the training application.

Currently includes a dynamic form for taking quizzes. The form is built
dynamically based on the questions provided and uses radio buttons for
answer selection.
"""

from django import forms
from .models import Question


class QuizForm(forms.Form):
    """Dynamic form for taking a quiz.

    The form takes a list of ``Question`` instances and constructs a set of
    ``ModelChoiceField`` fields, one for each question. The choices for
    each field are derived from the related ``Choice`` objects.
    """

    def __init__(self, *args, **kwargs) -> None:
        questions = kwargs.pop('questions', [])
        super().__init__(*args, **kwargs)
        for question in questions:
            field_name = f'question_{question.id}'
            self.fields[field_name] = forms.ModelChoiceField(
                queryset=question.choices.all(),
                widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
                label=question.text,
                empty_label=None,
                error_messages={'required': 'Выберите один вариант ответа.'},
            )
