from django.shortcuts import render
import json

from django.contrib.auth.models import User
from django.http import JsonResponse


from projects.models import Project
from rest_framework import viewsets, status
from .serializers import Projectser
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

@api_view(['GET'],)
def projectlist(request):
    projects=Project.objects.all()

    serializer = Projectser( projects,many=True)

    return Response(serializer.data)


@api_view(['GET'], )
def getproject(request,id):
    project = Project.objects.get(id=id)
    serializer = Projectser(project, many=False)

    return Response(serializer.data)

@api_view(['POST'],)
def createproject(request):

    serializer = Projectser(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return JsonResponse({'status': 'failed'})


@api_view(['PUT'],)
def updateapi(request,id):
    project = Project.objects.get(id=id)
    data = request.data
    serializer = Projectser(project, data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        print(serializer.errors)
        return JsonResponse({'status': 'failed'})



@api_view(['DELETE'],)
def deleteapiview(request,id):
    project=Project.objects.filter(id=id)
    if project:
        project.delete()
        return JsonResponse({'status':'ok'})
    return JsonResponse(Projectser.errors)
