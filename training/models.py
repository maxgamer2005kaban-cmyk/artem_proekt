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
    attck_id = models.CharField(max_length=20, blank=True, help_text='Идентификатор техники из MITRE ATT&CK')

    class Meta:
        ordering = ['title']
        verbose_name = 'техника'
        verbose_name_plural = 'техники'

    def __str__(self) -> str:
        return self.title


class Quiz(models.Model):
    """A quiz associated with a technique. Contains multiple questions."""

    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=200)

    class Meta:
        ordering = ['title']
        verbose_name = 'тест'
        verbose_name_plural = 'тесты'

    def __str__(self) -> str:
        return f"{self.technique.title}: {self.title}"


class Question(models.Model):
    """A question within a quiz."""

    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField(max_length=500)

    class Meta:
        ordering = ['id']
        verbose_name = 'вопрос'
        verbose_name_plural = 'вопросы'

    def __str__(self) -> str:
        return self.text


class Choice(models.Model):
    """A possible answer for a question."""

    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']
        verbose_name = 'вариант ответа'
        verbose_name_plural = 'варианты ответов'

    def __str__(self) -> str:
        return self.text


class Lab(models.Model):
    """A lab exercise associated with a technique."""

    technique = models.ForeignKey(Technique, on_delete=models.CASCADE, related_name='labs')
    title = models.CharField(max_length=200)
    description = models.TextField()
    instructions = models.TextField(help_text='Пошаговая инструкция для лабораторной работы')

    class Meta:
        ordering = ['title']
        verbose_name = 'лабораторная работа'
        verbose_name_plural = 'лабораторные работы'

    def __str__(self) -> str:
        return f"{self.technique.title}: {self.title}"
