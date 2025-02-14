from django.urls import path
from . import views

urlpatterns = [
    path('login_no_session/', views.login_sin_sesion, name='login_no_session'),
    path('login_session/', views.login_con_sesion, name='login_session'),
    path('inicio/', views.inicio, name='inicio'),
    path('logout/', views.logout_view, name='logout'),
]
