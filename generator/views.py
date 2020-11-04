from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    chars = list('abcdefghijklmnopqrstuvwxyz')
    length = int(request.GET.get('length'))
    pwd = ''
    if request.GET.get('uppercase'):
        chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('numbers'):
        chars.extend(list('0123456789'))
    if request.GET.get('special'):
        chars.extend(list('~!@#$%^&*()_+<>?'))
    for x in range(length):
        pwd += random.choice(chars)
    return render(request, 'generator/password.html', {'password':pwd})

def about(request):
    return render(request, 'generator/about.html')
