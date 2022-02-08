from tkinter import Image
from django.shortcuts import render
import json
import os
from posixpath import split
from unicodedata import name
from django.http import QueryDict
from django.utils import timezone

from rest_framework.views import APIView 

from rest_framework.response import Response
from rest_framework import status

from loadImage.serializer import SecondTSerializer
from loadImage.models import ImagenModelo


resexito= '{"message": "Exitoso"}'
reserror= '{"message": "Error"}'

def response_custom(responseData, stats, custom):
    Res =""
    if custom == "resexito":
        Res = json.loads(resexito)
    else:
        Res = json.loads(reserror)
    Res.update({'pay_load':responseData})
    Res.update({'status':stats}) 
    return Res


class ListaView(APIView):
    def get(self, request, format=None):
        querySet = ImagenModelo.objects.all()
        serializer = SecondTSerializer(querySet, many=True , context= {'request':request})
        return Response(response_custom(serializer.data, status.HTTP_200_OK,'reserror'))

    def post(self, request, format=None):        
        serializer = SecondTSerializer(data=request.data, context={"request":request})                                
        if serializer.is_valid():                        
           
            datos = request.data
            nameImg = str(datos.__getitem__('url_img')).split(".")
            datos.__setitem__('name_img',nameImg[0])
            datos.__setitem__('format_img',nameImg[1])
            serializer2 = SecondTSerializer(data=datos, context={"request":request})   

            if serializer2.is_valid():                                         
                serializer2.save()                
            return Response(response_custom(serializer2.data,status.HTTP_201_CREATED,'resexito'))
            
        else:        
           return Response(response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'reserror'))


class DetailView(APIView):
    
    def get_object(self,pk):
        try:
            return ImagenModelo.objects.get(pk=pk)
        except ImagenModelo.DoesNotExist:
            return 404

    def get(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = SecondTSerializer(idResponse,context={"request":request})            
            return Response(response_custom(serializer.data,status.HTTP_200_OK,'resexito'))
        else:                        
            return Response(response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST,'reserror'))
   
    def put(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = SecondTSerializer(idResponse, data=request.data, context={"request":request})            
            if serializer.is_valid():                
               
                datos = request.data               
                nameImg = str(datos.__getitem__('url_img')).split(".")
                datos.__setitem__('name_img',nameImg[0])
                datos.__setitem__('format_img',nameImg[1])
                datos.__setitem__('edit', timezone.now())
                serializer2 = SecondTSerializer(idResponse, data=datos, context={"request":request})  
                 
                if serializer2.is_valid():                               
                    serializer2.save()                                                         
                return Response(response_custom(serializer.data,status.HTTP_200_OK,'resexito'))
            else:                
                return Response(response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'reserror'))
        else:            
            return Response(response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST,'reserror'))
    
    def delete(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = SecondTSerializer(idResponse, data=request.data, context={"request":request})
            if serializer.is_valid():                
                datos = serializer.data               
                delImg = str(datos.__getitem__('url_img')).split("/")                
                file_path = "assets/img/"+delImg[-1]

                if os.path.isfile(file_path):
                   os.remove(file_path)                    
                idResponse.delete()                     
                return Response(response_custom(serializer.data,status.HTTP_200_OK,'resexito'))
            else:                
                return Response(response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'reserror'))
        else:            
            return Response(response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST,'reserror'))

