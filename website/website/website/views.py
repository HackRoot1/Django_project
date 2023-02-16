from django.http import HttpResponse
from django.shortcuts import render,redirect
from my_model.models import MyModel

def home(request):
    formData = MyModel.objects.all()
    data = {
        'formData': formData
    }
    return render(request, "index.html", data)

def subject1(request, sem):
    formData = MyModel.objects.filter(semester=sem).values()
    # formData = MyModel.objects.all[semester==sem]
    data = {
        'formData': formData
    }
    return render(request, "subject1.html", data)
def subject2(request):
    return render(request, "subject2.html")
def subject3(request):
    return render(request, "subject3.html")
def login(request):
    return render(request, "login.html")

def units(request):
    return render(request, "units.html")

def reference_books(request):
    return render(request, "reference_books.html")