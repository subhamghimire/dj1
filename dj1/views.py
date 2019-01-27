from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')


def contact(request):
    return HttpResponse('<h2>This is my contact</h2>subham.ghimire26@gmail.com')
