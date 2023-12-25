from .models import Course, Subject, Instructor
from django.forms import ModelForm, TextInput, EmailInput, Select, SelectMultiple


class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_name', 'instructor', 'subjects']
        widgets = {
            'course_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название курса'
            }),
            'instructor': TextInput(),
            'subjects': TextInput()
        }


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['instructor', 'subject_name']
        widgets = {
            'instructor': TextInput(),
            'subject_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета'
            })}


class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['instructor_name', 'instructor_id', 'email']

        widgets = {
            "instructor_name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя преподавателя'
            }),
            "instructor_id": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Id преподавателя'
            }),
            "email": EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите email'
            })
        }