from django.shortcuts import render
import json
import random


def getid(li):
    i = random.randint(0, 1000)
    if i in li:
        getid(li)
    return i


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


def persons(request, project):
    if project == "search":
        return render(request, 'main/persons.html')
    else:
        with open('main/persons.json', 'r', encoding='utf-8') as fx:
            personsin = json.load(fx)
            fx.close()
        return render(request, 'main/personsinfo.html', {'x': personsin, 'y': project})


def steps(request, project):
    if project == "search":
        return render(request, 'main/steps.html')
    else:
        with open('main/steps.json', 'r', encoding='utf-8') as fr:
            stepsin = json.load(fr)
            fr.close()
        return render(request, 'main/stepsinfo.html', {'x': stepsin, 'y': project})


def login(request):
    return render(request, 'main/loginpage.html')


def auth(request):
    if request.POST:
        with open('main/admininfo.json', 'r', encoding='utf-8') as fr:
            logininfo = json.load(fr)
            fr.close()
        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()
        for i in logininfo:
            if i["login"] == request.POST.get("login") and i["password"] == request.POST.get("password"):
                return render(request, 'main/adminpage.html',
                              {'access': i["acclevel"], 'project': i["project"], 'persons': pers})
    return render(request, 'main/loginpage.html')


def personsinfo(request):
    key = request.POST.get("key")
    print("HELLO", key)
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
        with open('main/idspers.json', 'r', encoding='utf-8') as fr:
            ids = json.load(fr)
            fr.close()
        idi = getid(ids)
        ids.append(idi)
        with open('main/idspers.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(ids, indent=4))
            file.close()
        d = {
            "id": idi,
            "project": [project],
            "name": name,
            "surname": surname,
            "fath_name": middlename,
            "dob": dob,
            "role": role

        }

        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            pers.append(d)
            file.close()

        with open('main/persons.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(pers, indent=4))
            file.close()

        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()

        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin", 'persons': d})
        return render(request, 'main/adminpage.html',
                      {'access': "manager", 'project': request.POST.get("projectname"), 'persons': pers})
    return render(request, 'main/loginpage.html')


def addadmin(request):
    if request.POST:
        login = request.POST.get("login")
        password = request.POST.get("password")
        acclevel = request.POST.get("acclevel")
        project = request.POST.get("project")
        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()

        d = {
            "login": login,
            "password": password,
            "acclevel": acclevel,
            "project": project

        }

        with open('main/admininfo.json', 'r', encoding='utf-8') as file:
            admins = json.load(file)
            admins.append(d)
            file.close()
        with open('main/admininfo.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(admins, indent=4))
            file.close()

        return render(request, 'main/adminpage.html', {'access': "admin", 'persons': pers})
    return render(request, 'main/loginpage.html')


def addstep(request):
    if request.POST:
        with open('main/idsst.json', 'r', encoding='utf-8') as fr:
            ids = json.load(fr)
            fr.close()
        project = request.POST.get("projectname")
        idi = getid(ids)
        ids.append(idi)
        with open('main/idsst.json', 'w', encoding='utf-8') as fr:
            fr.write(json.dumps(ids, indent=4))
            fr.close()
        num = request.POST.get("num")
        name = request.POST.get("pname")
        desc = request.POST.get("desc")
        dos = request.POST.get("dos")
        doe = request.POST.get("doe")
        status = request.POST.get("status")
        editor = request.POST.get("who")

        d = {
            "project": project,
            "id": str(idi),
            "num": num,
            "name": name,
            "desc": desc,
            "dos": dos,
            "doe": doe,
            "status": status

        }
        with open('main/steps.json', 'r', encoding='utf-8') as file:
            st = json.load(file)
            st.append(d)
            file.close()
        with open('main/steps.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(st, indent=4))
            file.close()

        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()

        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin", 'persons': pers})
        return render(request, 'main/adminpage.html',
                      {'access': "manager", 'project': request.POST.get("projectname"), 'persons': pers})
    return render(request, 'main/loginpage.html')


def addproject(request):
    with open('main/idsproj.json', 'r', encoding='utf-8') as fr:
        ids = json.load(fr)
        fr.close()

    if request.POST:
        idi = getid(ids)
        ids.append(idi)
        with open('main/idsproj.json', 'w', encoding='utf-8') as fr:
            fr.write(json.dumps(ids, indent=4))
            fr.close()
        name = request.POST.get("name")
        dos = request.POST.get("dos")
        doe = request.POST.get("doe")

        d = {
            "id": str(idi),
            "name": name,
            "start": dos,
            "end": doe
        }

        with open('main/projects.json', 'r', encoding='utf-8') as file:
            proj = json.load(file)
            proj.append(d)
            file.close()

        print(proj)
        with open('main/projects.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(proj, indent=4))
            file.close()
        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()
        return render(request, 'main/adminpage.html', {'access': "admin", 'persons': pers})
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
            if int(id) == int(step["id"]):
                step["status"] = new_status

        print(stepsin)
        with open('main/steps.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(stepsin, indent=4))
            file.close()
        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()
        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin", 'persons': pers})
        return render(request, 'main/adminpage.html',
                      {'access': "manager", 'project': request.POST.get("projectname"), 'persons': pers})
    return render(request, 'main/loginpage.html')


def addexperson(request):
    if request.POST:
        id = request.POST.get('persel')
        editor = request.POST.get("who")
        with open('main/persons.json', 'r', encoding='utf-8') as file:
            pers = json.load(file)
            file.close()
        for per in pers:
            if per['id'] == int(id):
                per['project'].append(request.POST.get('project'))

        with open('main/persons.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(pers, indent=4))
            file.close()

        with open('main/persons.json', 'r', encoding='utf-8') as file:
            d = json.load(file)
            file.close()

        if editor == "admin":
            return render(request, 'main/adminpage.html', {'access': "admin", 'persons': d})
        return render(request, 'main/adminpage.html',
                      {'access': "manager", 'project': request.POST.get("project"), 'persons': d})
    return render(request, 'main/loginpage.html')
