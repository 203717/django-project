from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from register.serializers import RegisterSerializer
from Profile.models import Profile
from Profile.serializers import ProfileSeria, RegisSeria
import json
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView 
import os
# Create your views here.

class RegisterIdView(APIView):
    

    def get_objectU(self,pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return 404  
    
    def get_objectP(self,pk):
        try:
            return Profile.objects.get(id_user_profile=pk)
        except Profile.DoesNotExist:
            return 404  
     

    def get(self,request,pk,format=None):
        idResponse = self.get_objectU(pk)

        if idResponse != 404:

            serializer = RegisterSerializer(idResponse,context={"request":request})
            idResponseP = self.get_objectP(pk)

            if idResponseP != 404:
                serializerP = ProfileSeria(idResponseP,context={"request":request})
               
                respuesta = json.dumps(serializer.data)
                respuesta = json.loads(respuesta)
                respuesta.update({"img_profile":serializerP.data.__getitem__("img_profile")})                
                
                return Response(respuesta)
            else:                                 
                respuesta = json.dumps(serializer.data)                
                respuesta = json.loads(respuesta)
                respuesta.update( {"img_profile":None})
                return Response(respuesta)

        else:                        
            return Response(status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        idResponse = self.get_objectU(pk)
        idResponseP = self.get_objectP(pk)             
                       
        if idResponse != 404 and idResponseP != 404:       
            user = RegisSeria(idResponse,data=request.data, context={"request":request}) 
            profil =ProfileSeria(idResponseP,data=request.data, context={"request":request})                                    
                        
            if profil.is_valid() and user.is_valid():                            

                if "img_profile" in request.data:
                    
                    nameImg = str(idResponseP.img_profile).split("/")[1]                
                    
                    file_path = "assets/img_profile/"+nameImg
                    if os.path.isfile(file_path):                                            
                        os.remove(file_path)                       
                    
                user.save()                  
                profil.save()    
                       
                return Response(status.HTTP_200_OK)
            else:     
                return Response(status.HTTP_400_BAD_REQUEST)
        else:            
            return Response("Id no encontrado",status.HTTP_400_BAD_REQUEST) 