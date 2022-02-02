
from dataclasses import fields
from pyexpat import model
from rest_framework import serializers    

#importacion de modelos
from primerComponente.models import PrimerModelo


class PrimerTablaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrimerModelo
        fields = ('campo_uno','edad')