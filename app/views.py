from django.shortcuts import render

# Create your views here.
def teacher(request):
    return render(request,'teacher.html')
def student(request):
    return render(request,'student.html')