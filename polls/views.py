
from django.shortcuts import render , HttpResponse
from .forms import add_student_form
from .models import student
# Create your views here.

def index(request):
    return render(request, 'polls/index.html')
def help(request):
    return render(request,'polls/help.html')

def add(request):
    if 'nam' in request.GET:
        return HttpResponse('the name is: '+request.GET['nam'])

def add_student(request):
    if request.method == 'POST':
        data = add_student_form(request.POST)
        if data.is_valid():
            na = data.cleaned_data['name']
            fna = data.cleaned_data['fname']
            rol = data.cleaned_data['rollNo']
            s = student(na,fna,rol)
            s.save()
        HttpResponse("OK all is well")
    else:
        data = add_student_form()
    return render(request, 'polls/add_student.html',{'form':data})
