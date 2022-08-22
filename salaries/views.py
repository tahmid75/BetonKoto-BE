
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from companies.models import Company, District
from position.models import Position, Level
from salaries.models import Salary

# Create your views here.

@api_view(['POST'])
@permission_classes((IsAuthenticated,))

def addSalary(request):
    try:
        user = User.objects.get(username=request.user)
        company = Company.objects.get(id=request.data['company'])
        position = Position.objects.get(id = request.data['position'])
        location = District.objects.get(id = request.data['district'])
        level = Level.objects.get(level = request.data['level'])
        salaryAmount = request.data['salary']
        
        salary = Salary()
        salary.user = user
        salary.company = company
        salary.position = position
        salary.level = level
        salary.location = location
        salary.salary = salaryAmount
        salary.save()

        return Response({'Success'})
    except:
        return Response({'Failed'})
