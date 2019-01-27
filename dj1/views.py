from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html' , {'name':'this is subham ghimire'})


def contact(request):
    return HttpResponse('<h2>This is my contact</h2>subham.ghimire26@gmail.com')
