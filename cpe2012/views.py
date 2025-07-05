

from django.shortcuts import render

def hello_world(request):
    return render(request, 'base.html')

def About(request):
    return render(request, 'About.html')

def FAQ(request):
    return render(request, 'FAQ.html')

def contact(request):
    return render(request, 'contact.html')