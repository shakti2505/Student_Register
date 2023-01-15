from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import  Student
from .forms import StudentForm

# Create your views here.

# This function  will add new data and render them.
def add_show(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            nm=form.cleaned_data['name']
            em=form.cleaned_data['email']
            rl=form.cleaned_data['roll_no']
            strd=form.cleaned_data['strd']
            reg = Student(name=nm, email=em, roll_no=rl, strd=strd)
            reg.save()
            form = StudentForm()
    else:
        form = StudentForm()
    stu = Student.objects.all()

    return render(request, 'enroll/add_and_show.html', {'form':form, 'stu':stu})



def Delete_student(request, id):
    if request.method=='POST':
        sd = Student.objects.get(pk=id)
        sd.delete()
        return HttpResponseRedirect('/')

# this function edit and update theb daata
def update_data(request, id):
    if request.method =='POST':
        sd = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=sd) 
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')
    else:
        sd = Student.objects.get(pk=id)
        form = StudentForm(instance=sd) 
    return render(request, 'enroll/update_student.html', {'form':form})       


