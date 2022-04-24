from django.shortcuts import render
import random

def about(request):
    return render(request, 'generator/about.html')

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    characters = list('abcdefghijklmnñopqrstuvwxyz')
    password_generated = ''
    
    length = int(request.GET.get('length'))
    
    if request.GET.get('uppercase'):
        characters.extend('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')
    if request.GET.get('special'):
        characters.extend('-_+!@#$%[]()^*/\|{}?=')
    if request.GET.get('numerics'):
        characters.extend('0123456789')
    
    for x in range(length):
        password_generated += random.choice(characters)
        
    context = {'password': password_generated}
    
    return render(request, 'generator/password.html', context)