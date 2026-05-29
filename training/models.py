"""
Models for the training application.

These models represent MITRE ATT&CK techniques, quizzes consisting of
questions and choices, and lab exercises. The relationships are kept
simple to be approachable for newcomers while demonstrating the power of
Django's ORM.
"""

from django.db import models


class Technique(models.Model):
    """Represents a MITRE ATT&CK technique with a title and description."""

    title = models.CharField(max_length=200)
    description = models.TextField()
    attck_id = models.CharField(max_length=20, blank=True, help_text='Identifier from the MITRE ATT&CK catalog')

    class Meta:
        ordering = ['title']
        verbose_name = 'Technique'
        verbose_name_plural = 'Techniques'

    def __str__(self) -> str:
        return self.title


class Quiz(models.Model):
    """A quiz associated with a technique. Contains multiple questions."""

    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'Quiz'
        verbose_name_plural = 'Quizzes'

    def __str__(self) -> str:
        return f"{self.technique.title}: {self.title}"


class Question(models.Model):
    """A question within a quiz."""

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self) -> str:
        return self.text


class Choice(models.Model):
    """A possible answer for a question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self) -> str:
        return self.text


class Lab(models.Model):
    """A lab exercise associated with a technique."""

    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='labs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField(help_text='Step-by-step instructions for the lab')

    class Meta:
        ordering = ['title']
        verbose_name = 'Lab'
        verbose_name_plural = 'Labs'

    def __str__(self) -> str:
        return f"{self.technique.title}: {self.title}"