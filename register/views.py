import json
from rest_framework.views import APIView 
from rest_framework import status
from django.contrib.auth.models import User

from .serializers import RegisterSerializer
from rest_framework.response import Response

resexito= '{"message": "Exitoso"}'
reserror= '{"message": "Error"}'


def response_custom(responseData, stats, custom ):
    Res =""
    if custom == "resexito":
        Res = json.loads(resexito)
    else:
        Res = json.loads(reserror)
    Res.update({'pay_load':responseData})
    Res.update({'status':stats}) 
    return Res

class RegistroView(APIView):
    def post(self, request, format=None):       
        serializer=RegisterSerializer(data=request.data, context={'request':request})
        if serializer.is_valid():
            datos = request.data               
            username = str(datos.__getitem__('username'))
            email = str(datos.__getitem__('email'))
            password = str(datos.__getitem__('password'))            
                        
            user = User(
            username = username,
            email = email
            )
    
            user.set_password(password)
            user.is_superuser = False
            user.is_staff = True
            user.save()    

            return Response(response_custom(serializer.data,status.HTTP_201_CREATED,'resexito'))
        else:
            return Response(response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'reserror'))
    
    def get(self, request, format=None):
        querySet = User.objects.all()
        serializer =RegisterSerializer(querySet, many=True , context= {'request':request})        
        return Response(response_custom('succes',serializer.data, status.HTTP_200_OK))
