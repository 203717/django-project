from rest_framework.views import APIView 
from rest_framework.response import Response

from rest_framework import status

# Create your views here.

#importacion de serealizadores
from primerComponente.serializers import PrimerTablaSerializer
#importacion de modelos
from primerComponente.models import PrimerModelo

import json

def res_custom(custom, responseData, stats):
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
            return Response(res_custom.response_custom(serializer.data,status.HTTP_201_CREATED,'resbien'))
        else:
            return Response(res_custom.response_custom(serializer.errors,status.HTTP_400_BAD_REQUEST,'resmal'))
            
    
       