from django.http import HttpResponse
from django.shortcuts import render,redirect

def home(request):
    return render(request, "index.html")

def subject1(request):
    return render(request, "subject1.html")
def subject2(request):
    return render(request, "subject2.html")
def subject3(request):
    return render(request, "subject3.html")
def subject4(request):
    return render(request, "subject4.html")

def units(request):
    return render(request, "units.html")

def reference_books(request):
    return render(request, "reference_books.html")