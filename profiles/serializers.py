from rest_framework.serializers import ModelSerializer, Serializer
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model

from profiles.models import Profile
from .models import Company, Position

class UserSerializer(ModelSerializer):
    class Meta:
        model  = User
        fields = '__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model  = Company
        fields = '__all__'

class PositionSerializer(ModelSerializer):
    class Meta:
        model  = Position
        fields = '__all__'

class ProfileSerializer(ModelSerializer):

    user = UserSerializer()
    company = CompanySerializer()
    position = PositionSerializer()
    
    class Meta:
        model = Profile
        fields = ['user', 'phone', 'gender', 'company', 'position', 'salary']
