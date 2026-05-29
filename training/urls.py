"""
URL configuration for the training app.

This module defines route patterns for listing techniques, viewing
individual techniques and their associated quizzes/labs, taking quizzes,
viewing quiz results, and viewing lab details.
"""

from django.urls import path
from . import views


app_name = 'training'

urlpatterns = [
    path('', views.TechniqueListView.as_view(), name='technique_list'),
    path('technique/<int:pk>/', views.TechniqueDetailView.as_view(), name='technique_detail'),
    path('lab/<int:pk>/', views.LabDetailView.as_view(), name='lab_detail'),
    path('quiz/<int:pk>/', views.quiz_view, name='quiz'),
    path('quiz/<int:pk>/results/', views.quiz_result_view, name='quiz_results'),
]