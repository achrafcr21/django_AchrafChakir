from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def prof(request):
    teachers = {
        "prof1": {"name": "Roger", "surname": "Sobrino", "age": "23"}
    }
    context = {'t': teachers}
    return render(request, 'proff.html', context)

def users(request):
    users = [
        {"name": "Oriol", "surname": "Roca", "age": "18"},
        {"name": "Anna", "surname": "Martínez", "age": "20"}
    ]
    context = {'usrs': users}
    return render(request, 'users.html', context)


def index_one(request):
    return render(request, 'index.html')