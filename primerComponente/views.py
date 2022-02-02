from rest_framework.views import APIView 
from rest_framework.response import Response

from rest_framework import status

# Create your views here.

#importacion de serealizadores
from primerComponente.serializers import PrimerTablaSerializer
#importacion de modelos
from primerComponente.models import PrimerModelo

import json

def response_custom(custom, responseData, stats):
        respuesta ={}
        if custom == "succes":
            respuesta = json.loads(resexito)
        else:
            respuesta = json.loads(reserror)

        respuesta.update({'pay_load':responseData})
        respuesta.update({'status':stats}) 

        return respuesta

resexito= '{"message": "Exitoso"}'
reserror= '{"message": "Error"}'

resbien= json.loads(resexito)
resmal = json.loads(reserror)

class PrimerViewList(APIView):
        
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializer(querySet,many=True , context={'request':request})
        #print(responser_custom('succes',serializer.data,'good'))    
        return Response(serializer.data)
        return Response(responser_custom('succes',serializer.data, status.HTTP_200_OK))

    def post(self, request, format=None):
        serializer = PrimerTablaSerializer(data=request.data, context={"request":request})
        if serializer.is_valid():
            serializer.save()            
            return Response(response_custom.response_custom(serializer.data,status.HTTP_201_CREATED,'resbien'))
        else:
            return Response(response_custom.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'resmal'))
            
class PrimerViewDetail(APIView):
    
    def get_object(self,pk):
        try:
            return PrimerModelo.objects.get(pk=pk)
        except PrimerModelo.DoesNotExist:
            return 404


    def get(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse,context={"request":request})
            
            return Response(response_custom(serializer.data,status.HTTP_200_OK, 'resbien'))
            #return response(serializer.data, status=status.HTTP_200_OK)
            #return Response(serializer.data, status=status.HTTP_200_OK)
        else:            
            #return Response("no encontrado",status=status.HTTP_400_BAD_REQUEST)
            return Response(response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST, 'resmal'))
    
    def put(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, data=request.data, context={"request":request})
            if serializer.is_valid():                
                serializer.save()
                #return response(serializer.data, status=status.HTTP_200_OK)
                return Response(response_custom(serializer.data,status.HTTP_200_OK,'resbien'))
            else:
                #return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
                return Response(response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'resmal'))
        else:
            #retunr Response("no encontrado",status=status.HTTP_400_BAD_REQUEST)
            #return Response("no encontrado",status=status.HTTP_400_BAD_REQUEST)
            return Response(response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST,'resmal'))

    def delete(self,request,pk,format=None):
        idResponse = self.get_object(pk)        
        if idResponse != 404:
            serializer = PrimerTablaSerializer(idResponse, data=request.data, context={"request":request})
            if serializer.is_valid():                
                idResponse.delete()
                
                return Response(response_custom('succes',serializer.data,status.HTTP_200_OK,'resbien'))
                #return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(response_custom('error',serializer.errors,status.HTTP_400_BAD_REQUEST))
        else:
            return Response(response_custom("ID no encontrado",status.HTTP_400_BAD_REQUEST, 'resmal'))
       