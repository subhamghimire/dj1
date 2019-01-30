from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html' , {'name':'this is subham ghimire','address':'hetaudachildrenpark'})

def count(request):
    return render(request, 'count.html')
