from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Company, District
from .serializers import CompanySerializer, SingleCompanySerializer, DistrictSerializer, CompanySerializerTrimmed
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def allCompanies(request):
    companies = Company.objects.all()
    serializer = CompanySerializer(companies,  many=True)
    return Response(serializer.data)

@api_view(['GET'])
def allCompaniesTrimmed(request):
    companies = Company.objects.all().values('id', 'name')
    serializer = CompanySerializerTrimmed(companies,  many=True)
    return Response(serializer.data)

@api_view(['GET'])
def allLocations(request):
    locations = District.objects.all()
    serializer = DistrictSerializer(locations,  many=True)
    return Response(serializer.data)


@api_view(['GET'])
def companyDetails(request, id):
    company = Company.objects.get(id=id)
    serializer = SingleCompanySerializer(company)
    return Response(serializer.data)

