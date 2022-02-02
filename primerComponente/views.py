from rest_framework.views import APIView 
from rest_framework.response import Response

# Create your views here.

#importacion de modelos
from primerComponente.models import PrimerModelo


#importacion de serealizadores
from primerComponente.serializers import PrimerTablaSerializer

class PrimerViewList(APIView):
        
    def get(self, request, format=None):
        querySet = PrimerModelo.objects.all()
        serializer = PrimerTablaSerializer(querySet,many=True , context={'request':request})
        #print(responser_custom('succes',serializer.data,'good'))    
        return Response(serializer.data)
       