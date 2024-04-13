from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm

def index(request):
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = StudentForm()
    return render(request, 'index.html', {'form': form,'students':Student.objects.all()})