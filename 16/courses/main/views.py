from django.shortcuts import render, redirect
from .models import Course, Subject, Instructor
from .forms import CourseForm, SubjectForm, InstructorForm
from django.shortcuts import render, redirect
def index(request):
    return render(request, 'main/index.html')

def courses(request):
    course = Course.objects.all()
    return render(request, 'main/courses.html', {'course': course})

def subject(request):
    subject = Subject.objects.all()
    return render(request, 'main/subject.html',{'subject': subject})

def instructor(request):
    instructor = Instructor.objects.all()
    return render(request, 'main/instructor.html', {'instructor': instructor})


def table(request):
    instructors = Instructor.objects.all()
    subjects = Subject.objects.all()
    courses = Course.objects.all()

    return render(request, 'main/table.html', {
        'instructors': instructors,
        'subjects': subjects,
        'courses': courses,
    })

def add_courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CourseForm()
    data = {
        'form': form
    }
    return render(request, 'main/add_courses.html', data)

def add_subject(request):
    error = ''
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Вы неверно заполнили данные"
    else:
        form = SubjectForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_subject.html', data)

def add_instructor(request):
    error = ''
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = "Вы неверно заполнили данные"
    else:
        form = InstructorForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/add_instructor.html', data)