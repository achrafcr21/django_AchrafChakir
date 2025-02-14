from django.shortcuts import render, redirect

def guardar_sesion(request):
    request.session['usuario'] = 'Juan'
    return render(request, 'guardar_sesion.html')

def recuperar_sesion(request):
    usuario = request.session.get('usuario', 'Invitado')
    return render(request, 'recuperar_sesion.html', {'usuario': usuario})

def eliminar_sesion(request):
    # Eliminar un valor de la sesión
    if 'usuario' in request.session:
        del request.session['usuario']
    return redirect('recuperar_sesion')
