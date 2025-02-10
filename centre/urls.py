from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_one, name='index_one'),  # Página principal de 'centre'
    path('students/', views.students, name='students'),  # Página de estudiantes
    path('teachers/', views.teachers, name='teachers'),  # Página de profesores
]