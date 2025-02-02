from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_one, name='index_one'),  # Página principal de 'centre'
    path('prof/', views.prof, name='prof'),      # Página del profesor
    path('users/', views.users, name='users'),   # Página de usuarios
]