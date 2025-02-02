from django.shortcuts import render

def teachers(request):
    teachers = [
        {"id": 1, "name": "Roger", "surname": "Sobrino", "age": 39, "role": "teacher", "courses": ["DAW2B", "DAW2A"]},
        {"id": 2, "name": "Josep Oriol", "surname": "Roca", "age": 25, "role": "teacher", "courses": ["DAW2B", "DAW2A", "DAW1A"]},
        {"id": 3, "name": "Juanma", "surname": "Biel", "age": 24, "role": "teacher", "courses": ["DAW2B", "DAW2A"]},
    ]
    context = {'teachers': teachers}
    return render(request, 'teachers.html', context)

def students(request):
    students = [
        {"id": 1, "name": "Achraf", "surname": "Chakir", "age": 21, "role": "student", "modules": ["M07", "M08"]},
        {"id": 2, "name": "Adrian", "Navarro": "Student", "age": 20, "role": "student", "modules": ["M07", "M09"]},
        {"id": 3, "name": "Xavier", "delpino": "Student", "age": 20, "role": "student", "modules": ["M07", "M08", "M09"]},
    ]
    context = {'students': students}
    return render(request, 'students.html', context)

def index_one(request):
    return render(request, 'index.html')