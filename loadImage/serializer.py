from dataclasses import fields
from rest_framework import serializers    

#models
from loadImage.models import ImagenModelo

class SecondTSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenModelo
        fields = ('__all__')