from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import database
from .seriallizer import databaseSerializer

# Create your views here.

class databaseView(APIView):
    def get(self, request,format=None):
        data = database.objects.all().order_by('-id')
        serializer = databaseSerializer(data, many=True)
        return Response({'ok': True, 'data':serializer.data},status=200)
    

    def post(self, request, format=None):
        serializer = databaseSerializer (data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'ok': True, 'data':serializer.data} , status=200)
        return Response({'ok': False,  'errors': serializer.errors})
    
    def patch(self , request, format=None):
        try:
            database_instance = database.objects.get(id=request.data['id'])
            serializer = databaseSerializer(database_instance, data=request.data, partial= True)
            if serializer.is_valid():
                serializer.save()
                return Response({'ok': True, 'data':serializer.data, 'msg': 'Update Success!'})
            return Response ({'ok': False, 'errors': serializer.errors})
        except:
            return Response({'ok': False, 'msg': 'Database not found!'})
        
    def delete(self, request, format=None):
       database_instance = database.objects.get(id=request.data['id'])

       database_instance.delete()
       return Response("Deleted")