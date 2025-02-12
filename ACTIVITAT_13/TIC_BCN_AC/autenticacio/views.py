from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import LoginForm
from .models import Usuario

# Create your views here.

def login_sin_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email, password=password)
                return redirect('inicio')
            except Usuario.DoesNotExist:
                messages.error(request, 'Credenciales incorrectas')
    else:
        form = LoginForm()
    return render(request, 'autenticacio/login.html', {'form': form})

def login_con_sesion(request):
    if request.session.get('usuario_id'):
        return redirect('inicio')
        
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email, password=password)
                request.session['usuario_id'] = usuario.id
                return redirect('inicio')
            except Usuario.DoesNotExist:
                messages.error(request, 'Credenciales incorrectas')
    else:
        form = LoginForm()
    return render(request, 'autenticacio/login.html', {'form': form})

def inicio(request):
    if request.session.get('usuario_id'):
        usuario = Usuario.objects.get(id=request.session['usuario_id'])
        return render(request, 'autenticacio/inicio.html', {'usuario': usuario})
    return redirect('login_session')

def logout_view(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    return redirect('login_session')
