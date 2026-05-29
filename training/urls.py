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
    path('method/', views.method_view, name='method'),
    path('matrix/', views.matrix_view, name='matrix'),
    path('quizzes/', views.quiz_catalog_view, name='quiz_catalog'),
    path('labs/', views.lab_catalog_view, name='lab_catalog'),
    path('soc/', views.soc_process_view, name='soc_process'),
    path('technique/<int:pk>/', views.TechniqueDetailView.as_view(section='theory'), name='technique_detail'),
    path('technique/<int:pk>/detection/', views.TechniqueDetailView.as_view(section='detection'), name='technique_detection'),
    path('technique/<int:pk>/quizzes/', views.TechniqueDetailView.as_view(section='quizzes'), name='technique_quizzes'),
    path('technique/<int:pk>/labs/', views.TechniqueDetailView.as_view(section='labs'), name='technique_labs'),
    path('lab/<int:pk>/', views.LabDetailView.as_view(), name='lab_detail'),
    path('quiz/<int:pk>/', views.quiz_view, name='quiz'),
    path('quiz/<int:pk>/results/', views.quiz_result_view, name='quiz_results'),
]
