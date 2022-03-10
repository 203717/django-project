from django.contrib.auth.models import User
from Profile.models import Profile
from rest_framework import serializers

class RegisSeria(serializers.ModelSerializer):

    class Meta:
       model = User
       fields = ('username', 'email', 'first_name', 'last_name')
       extra_kwargs = {
           'first_name': {'required': False},
           'last_name': {'required': False}
       }
   

class ProfileSeria(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id_user_profile', 'img_profile')