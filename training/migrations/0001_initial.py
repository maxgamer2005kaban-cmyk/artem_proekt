"""
Initial migration for the training app.

This migration defines database tables for techniques, quizzes, questions,
choices, and labs. It is generated manually based on the models defined
in ``training/models.py`` and should be applied before running the server
to avoid ``OperationalError: no such table`` issues.
"""

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('attck_id', models.CharField(blank=True, help_text='Identifier from the MITRE ATT&CK catalog', max_length=20)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Technique',
                'verbose_name_plural': 'Techniques',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzes', to='training.technique')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='training.quiz')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='training.question')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name': 'Choice',
                'verbose_name_plural': 'Choices',
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('instructions', models.TextField(help_text='Step-by-step instructions for the lab')),
                ('technique', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='labs', to='training.technique')),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Lab',
                'verbose_name_plural': 'Labs',
            },
        ),
    ]