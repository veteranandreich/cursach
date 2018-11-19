from django.shortcuts import render
import json

def index(request):
    with open('main/projects.json', 'r', encoding='utf-8') as fh:
        maininfo = json.load(fh)
        fh.close()

    with open('main/persons.json', 'r', encoding='utf-8') as fx:
        personsin = json.load(fx)
        fx.close()

    with open('main/steps.json', 'r', encoding='utf-8') as fr:
        stepsin = json.load(fr)
        fr.close()
    return render(request, 'main/mainpage.html', {'x': maininfo, 'y': personsin, 'z': stepsin})


def persons(request):
    return render(request, 'main/persons.html')


def steps(request):
    return render(request, 'main/steps.html')


def login(request):
    return render(request, 'main/loginpage.html')


def auth(request):
    if request.POST:
        with open('main/admininfo.json', 'r', encoding='utf-8') as fr:
            logininfo = json.load(fr)
            fr.close()
        for i in logininfo:
            if i["login"] == request.POST.get("login") and i["password"] == request.POST.get("password"):
                return render(request, 'main/adminpage.html', {'access': i["acclevel"], 'project': i["project"]})
    return render(request, 'main/loginpage.html')


def personsinfo(request):
    key = request.POST.get("key")
    with open('main/persons.json', 'r', encoding='utf-8') as fx:
        personsin = json.load(fx)
        fx.close()
    return render(request, 'main/personsinfo.html', {'x': personsin, 'y': key})


def stepsinfo(request):
    key = request.POST.get("key")
    with open('main/steps.json', 'r', encoding='utf-8') as fr:
        stepsin = json.load(fr)
        fr.close()
    return render(request, 'main/stepsinfo.html', {'x': stepsin, 'y': key})


def addperson(request):
    if request.POST:
        project = request.POST.get("projectname")
        name = request.POST.get("pname")
        surname = request.POST.get("surname")
        middlename = request.POST.get("middlename")
        dob = request.POST.get("dob")
        role = request.POST.get("role")
        editor = request.POST.get("who")
        d = {
            "project": project,
            "name": name,
            "surname": surname,
            "fath_name": middlename,
            "dob": dob,
            "role": role

        }
        f = open('main/persons.json').read()
        new_personin = f[:-3] + ',\n \n  ' + json.dumps(d, indent=4) + '\n \n]'
        new_personin = new_personin[:-5] + '  }\n\n]'
        with open('main/persons.json', 'w', encoding='utf-8') as file:
            file.write(new_personin)
            file.close()
        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin"})
        return render(request, 'main/adminpage.html', {'access': "manager", 'project': request.POST.get("projectname")})
    return render(request, 'main/loginpage.html')



def addadmin(request):
    if request.POST:
        login = request.POST.get("login")
        password = request.POST.get("password")
        acclevel = request.POST.get("acclevel")
        project = request.POST.get("project")

        d = {
        "login": login,
        "password": password,
        "acclevel": acclevel,
        "project": project

        }

        f = open('main/admininfo.json').read()
        new_personin = f[:-3] + ',\n \n  ' + json.dumps(d, indent=4) + '\n \n]'
        new_personin = new_personin[:-5] + '  }\n\n]'
        with open('main/admininfo.json', 'w', encoding='utf-8') as file:
            file.write(new_personin)
            file.close()
        return render(request, 'main/adminpage.html', {'access': "admin"})
    return render(request, 'main/loginpage.html')


def addstep(request):
    if request.POST:
        project = request.POST.get("projectname")
        id = request.POST.get("ID")
        num = request.POST.get("num")
        name = request.POST.get("pname")
        desc = request.POST.get("desc")
        dos = request.POST.get("dos")
        doe = request.POST.get("doe")
        status = request.POST.get("status")
        editor = request.POST.get("who")

        d = {
            "project": project,
            "id": id,
            "num": num,
            "name": name,
            "desc": desc,
            "dos": dos,
            "doe": doe,
            "status": status

        }

        f = open('main/steps.json').read()
        new_personin = f[:-3] + ',\n \n  ' + json.dumps(d, indent=4) + '\n \n]'
        new_personin = new_personin[:-5] + '  }\n\n]'
        with open('main/steps.json', 'w', encoding='utf-8') as file:
            file.write(new_personin)
            file.close()
        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin"})
        return render(request, 'main/adminpage.html', {'access': "manager", 'project': request.POST.get("projectname")})
    return render(request, 'main/loginpage.html')

def addproject(request):
    if request.POST:
        id = request.POST.get("ID")
        name = request.POST.get("name")
        dos = request.POST.get("dos")
        doe = request.POST.get("doe")

        d = {
        "id": id,
        "name": name,
        "start": dos,
        "end": doe

        }

        f = open('main/projects.json').read()
        new_personin = f[:-3] + ',\n \n  ' + json.dumps(d, indent=4) + '\n \n]'
        new_personin = new_personin[:-5] + '  }\n\n]'
        with open('main/projects.json', 'w', encoding='utf-8') as file:
            file.write(new_personin)
            file.close()
        return render(request, 'main/adminpage.html', {'access': "admin"})
    return render(request, 'main/loginpage.html')


def editstep(request):
    if request.POST:
        id = request.POST.get("ID")
        new_status = request.POST.get("status")
        editor = request.POST.get("who")

        with open('main/steps.json', 'r', encoding='utf-8') as fr:
            stepsin = json.load(fr)
            fr.close()

        for step in stepsin:
            if id == step["id"]:
                step["status"] = new_status


        with open('main/steps.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(stepsin[1:-1], indent=4))
            file.close()

        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin"})
        return render(request, 'main/adminpage.html', {'access': "manager", 'project': request.POST.get("projectname")})
    return render(request, 'main/loginpage.html')

