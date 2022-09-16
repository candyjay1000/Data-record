from django.shortcuts import render, redirect
from department.models import Department
from django.urls import reverse
from .forms import DepartmentForm
from django.contrib import messages




def indexpage(request):
    departments = Department.objects.all()
    context = {
        'department': departments
    }
    return render(request, 'department/index.html', context)


def add_department(request):
    form = DepartmentForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect(('add_section'))
    return render(request, 'department/add.html.html', context)


def delete_department(request, id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request, 'DEPARTMENT SUCCESSFULLY DELETED')
    return redirect(('indexpage'))


def update_department(request, id):
    instance = Department.objects.get(id=id)
    form = DepartmentForm(request.POST or None,
                             request.FILES or None, instance=instance)
    context = {
        'form': form
    }
    if form.is_valid():
        form.save()
        messages.success(request, 'DEPARTMENT SUCCESSFULLY UPDATED')
    return render(request, 'department/update.html', context)


 


