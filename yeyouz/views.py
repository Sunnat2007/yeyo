from django.shortcuts import render
from .models import *

# langluage

def base(request):
    return render(request , 'base.html' ,)
def baseuz(request):
    return render(request , 'baseuz.html' ,)
def baseen(request):
    return render(request , 'baseen.html' ,)

#ruskiy
def aktivnost(request):
    return render(request , 'aktivnost.html' ,)
def onas(request):
    return render(request , 'onas.html' ,)
def zakazat(request):
    return render(request , 'zakazat.html' ,)
def registr(request):
    return render(request , 'registr.html' ,)

#uzb
def faoliyat(request):
    return render(request , 'faoliyat.html' ,)
def haqimizda(request):
    return render(request , 'haqimizda.html' ,)
def buyurtma(request):
    return render(request , 'zakaz.html' ,)