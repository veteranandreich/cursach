from django.shortcuts import render
import json

with open('main/projects.json', 'r', encoding='utf-8') as fh:
    maininfo = json.load(fh)

with open('main/persons.json', 'r', encoding='utf-8') as fx:
    personsinfo = json.load(fx)



def index(request):
    return render(request, 'main/mainpage.html', {'x': maininfo})

def persons(request):
    a = str(request)
    a = a[20:-2]
    lastsl = a.index('/')
    a = a[:lastsl]
    return render(request, 'main/persons.html', {'x': personsinfo, 'sitename': a})

def steps(request):
    pass
    '''return render(request, 'main/steps.html', {'x': data})'''