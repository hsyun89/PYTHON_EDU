from django.shortcuts import render
from .models import Student

def index(request):
    students = Student.objects.all()
    return render(request, 'students/index.html', {'students':students})

def new(request):
    return render(request, 'students/new.html')

def create(request):
    name = request.POST.get('name')
    age = request.POST.get('age')
    email = request.POST.get('email')
    student = Student(name=name, age=age, email=email)
    student.save()
    
    return render(request, 'articles/create.html')
    # return redirect(f'/students/{student.pk}/')
