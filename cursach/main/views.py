from django.shortcuts import render
import json

with open('main/projects.json', 'r', encoding='utf-8') as fh:
    maininfo = json.load(fh)

with open('main/persons.json', 'r', encoding='utf-8') as fx:
    personsinfo = json.load(fx)

with open('main/steps.json', 'r', encoding='utf-8') as fr:
    stepsinfo = json.load(fr)


def index(request):
    return render(request, 'main/mainpage.html', {'x': maininfo})


def persons(request):
    a = str(request)
    a = a[20:-2]
    lastsl = a.index('/')
    a = a[:lastsl]
    return render(request, 'main/persons.html', {'x': personsinfo, 'sitename': a})


def steps(request):
    a = str(request)
    a = a[20:-2]
    return render(request, 'main/steps.html', {'x': stepsinfo, 'sitename': a})


def login(request):
    return render(request, 'main/loginpage.html')


def auth(request):
    print(request.POST.get('login'), "        CHECHNYA        ", request.POST.get('password'))
    logininfo = [
        {"login": "admin",
         "password": "admin"
         },

        {"login": "manager",
         "password": "manager"
         }
    ]
    if request.POST:
        for i in logininfo:
            if i["login"] == request.POST.get("login") and i["password"] == request.POST.get("password"):
                return render(request, 'main/adminpage.html')
    return render(request, 'main/mainpage.html', {'x': maininfo})
