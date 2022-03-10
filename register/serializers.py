from asyncio.windows_events import NULL
from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django import forms
from Profile.models import Profile
class FirstSerializerRegister(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('username', 'password', 'email')



class RegisterSerializer(serializers.ModelSerializer):
   email = serializers.EmailField(
           required=True,
           validators=[UniqueValidator(queryset=User.objects.all())]
           )
 
   password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
   password2 = serializers.CharField(write_only=True, required=True)

   class Meta:
       model = User
       fields = ('id','username', 'password', 'password2', 'email', 'first_name', 'last_name')
       extra_kwargs = {
           'first_name': {'required': True},
           'last_name': {'required': True}
       }


   def validate(self, attrs):
       if attrs['password'] != attrs['password2']:
           raise serializers.ValidationError({"password": "Password error"})
 
       return attrs
 
   def create(self, validated_data):
       
       user = User.objects.create(
           username=validated_data['username'],
           email=validated_data['email'],
           first_name=validated_data['first_name'],
           last_name=validated_data['last_name']
       )

       user.set_password(validated_data['password'])
       user.save()

       prof = Profile(
           id_user_profile = user,           
       )
       prof.save() 

       return user