from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model

from .models import Company, District

class DistrictSerializer(ModelSerializer):
    class Meta:
        model = District
        fields = '__all__'

class CompanySerializer(ModelSerializer):

    class Meta:
        model  = Company
        fields = ['id','name', 'website', 'description']

class CompanySerializerTrimmed(ModelSerializer):
    
    class Meta:
        model  = Company
        fields = ['id','name']

class SingleCompanySerializer(ModelSerializer):
    
    headquarter = DistrictSerializer()

    class Meta:
        model  = Company
        fields = ['id','name', 'headquarter', 'website', 'description']