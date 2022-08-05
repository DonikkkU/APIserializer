from django.shortcuts import render
from django.http import JsonResponse
from .models import *


def get_projects(requests):
    data = Project.objects.all().values()
    print(data[:2])
    print(type(data))
    print(list(data)[:2])
    response = {"projects": list(data)}
    return JsonResponse(response)

def get_project(requests, id):
    data = Project.objects.get(id=id)
    print(data)
    print('=========')
    print(type(data))
    print('=========')
    data = data.__dict__
    print(data)
    data.pop('_state', 'not found')
    response = data
    return JsonResponse(response)

def insert_tag(request, name):
    try:
        tag = Tag.objects.create(name=name)
    except Exception as error:
        data = {"ok": False, "error": str(error)}
    else:
        data = tag.__dict__
        data.pop('_state')
        data["ok"] = True
        data["error"] = ""
    return JsonResponse(data)


def insert_project(request):
    title = request.headers['title']
    definition = request.headers['definition']
    user = request.headers['user']
    try:
        project = Project.objects.create(title=title,
                                         description=definition,
                                         user_id=user
                                         )
    except Exception as error:
        data = {
            "error": str(error)
        }
        return JsonResponse(data)

    data = project.__dict__
    data.pop('_state', '')
    data.pop('image', '')  # rasmni jsonga o'girib bo'lmaydi
    return JsonResponse(data)

def delete_project(request, pk):
    project = Project.objects.get(id=pk)
    project.delete()
    return JsonResponse({"message": 'Project is deleted'})


def edit_project(request, pk):
    try:
        project = Project.objects.get(id=pk)
    except Exception as error:
        return JsonResponse({"error": str(error)})

    project.title = request.headers["title"]
    project.description = request.headers["definition"]
    project.save()
    data = project.__dict__
    data.pop('_state')
    data.pop('image')
    return JsonResponse(data)
