from rest_framework import serializers
from rest_framework.fields import SerializerMethodField
from .models import *

class CreateUserSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(source='first_name', required=False)
    lastName = serializers.CharField(source='last_name', required=False)
    isStaff = serializers.BooleanField(source='is_staff', default=False)

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    class Meta:
        model = CustomUser
        fields = ('email', 'password', 'firstName', 'lastName', 'isStaff')
        extra_kwargs = {
            'password': {'write_only': True}
        }