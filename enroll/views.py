from unicodedata import name
from django.shortcuts import render

from enroll.forms import StudentRegistration,TeacherRegistration
from enroll.models import User
# Create your views here.

def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['students_name']
            email = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']
            fm = User(students_name=name,email=email,password=pwd)
            fm.save()
            fm =StudentRegistration()
    else:
        fm = StudentRegistration()
    return render(request, 'enroll/addandshow.html', {"form":fm})

def teacher_registeration(request):
    if request.method == 'POST':
        fm = TeacherRegistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['teachers_name']
            email = fm.cleaned_data['email']
            pwd = fm.cleaned_data['password']   
            fm = User(teachers_name=name,email=email,password=pwd)
            fm.save()
            fm =TeacherRegistration()
    else:
        fm = TeacherRegistration()
    return render(request, 'enroll/teacher.html', {"form":fm})