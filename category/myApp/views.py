from django.shortcuts import render,redirect
from .models import Students
from .forms import StudentsForm

def listData(request):
    studentsForm = StudentsForm()
    students = Students.objects.all()
    context = {
        'studentsForm' : studentsForm,
        'students' : students
    }
    return render(request, 'myApp/index.html',context)
def writeData(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listData')
    else:
        form = StudentsForm()
    return render(request,"myApp/input.html",{'form':form})

def inputData(request):
    if request.method == 'POST':
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listData')
    return redirect('writeData')

def editData(request):
    id = request.GET['id']
    edit = Students.objects.get(id=id)
    return render(request,"myApp/update.html",{'edit':edit})

def updateData(request):
    beforeid = request.POST['beforeid']
    id = request.POST['id']
    if beforeid == id:
        update = Students.objects.get(id=id)
        update.firstname = request.POST['firstname']
        update.secondname = request.POST['secondname']
        update.age = request.POST['age']
        update.major = request.POST['major']
        update.address = request.POST['address']
        update.save()
    else:
        beforedata = Students.objects.get(id=beforeid).delete()
        update = StudentsForm(request.POST)
        update.save()
    return redirect('listData')

def deleteData(request):
    id = request.GET['id']
    delete = Students.objects.get(id=id).delete()
    return redirect('listData')


