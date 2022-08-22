from re import search
import re
from django.shortcuts import render
from django.http import HttpResponse
from django.urls.resolvers import LocaleRegexDescriptor
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.serializers import Serializer

from .models import Position, Profile, Company
from .serializers import ProfileSerializer, UserSerializer


@api_view(['POST'])
def createProfile(request):
    
    email = request.data['email']
    password = request.data['password']

    if(User.objects.filter(email=email).exists()):
        return Response("User exists")
    else:
        user= User()
        user.email= email
        user.username = email
        user.password = make_password(password)
        user.save()

        profile = Profile()
        profile.user = user
        profile.save()

        return Response("User created")

@api_view(['GET'])
@permission_classes((IsAuthenticated,)) #should be a tuple of classes
def viewProfile(request):
    username = request.user
    user = User.objects.get(username=username)
    if(Profile.objects.filter(user=user).exists()):
        profile = Profile.objects.get(user=user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    else:
        profile = Profile()
        profile.user = user
        profile.save()
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


@api_view(['POST'])
@permission_classes((IsAuthenticated,)) #should be a tuple of classes
def updateProfile(request):
    
    username = request.user
    user = User.objects.get(username=username)
    user.first_name = request.data['name']
    user.save()

    if(Profile.objects.filter(user=user).exists()):

        profile = Profile.objects.get(user=user)

        #change this to serializer later
        try:
            profile.phone = request.data['phone']
            profile.company = Company.objects.get(id=request.data['company'])
            profile.position = Position.objects.get(id=request.data['position'])
            profile.salary = request.data['salary']
            profile.save()
        except Exception as e:
            print(str(e))

        serializer = ProfileSerializer(profile)
        return Response(serializer.data)
    else:
        print("Something else")
        return Response("Error")

    