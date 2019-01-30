from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html' , {'name':'this is subham ghimire','address':'hetaudachildrenpark'})

def count(request):
    data = request.GET['tname']
    word_list = data.split()
    length = len(word_list)

    dictword = {}

    for word in word_list:
        if word in dictword:
            dictword[word] += 1
        else:
            dictword[word] = 1



    return render(request, 'count.html',{'text':data,'words':length ,'worddictionary':dictword})
