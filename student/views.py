from django.shortcuts import render, redirect
from student.models import Student
from django.urls import reverse
from .forms import StudentForm
from django.contrib import messages
# Create your views here.
def welcome(request):
    return render(request, 'student/welcome.html')

def students_indexpage(request):
    students =Student.objects.all()
    context = {
        'students': students
    }
    return render(request, 'student/index_student.html', context)


def add_student(request):
    form = StudentForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(('add_student'))
    return render(request, 'student/add_student.html', context)


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request, 'THE STUDENT PROFILE HAS BEEN DELETED')
    return redirect(('students_indexpage'))


def update_student(request, id):
    instance = Student.objects.get(id=id)
    form = StudentForm(request.POST or None,
                             request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'THE STUDENT HAS BEEN UPDATED')
    return render(request, 'student/update_student.html', context)


