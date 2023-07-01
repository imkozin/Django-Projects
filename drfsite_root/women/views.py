from django.shortcuts import render
from rest_framework import generics, status
from .models import Women
from .serializers import WomenSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

# Create your views here.

class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer

class WomenAPIView(APIView):
    def get(self, request):
        w = Women.objects.all()
        return Response({'posts' : WomenSerializer(w, many=True).data})
    
    def post(self, request):
        serializer = WomenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post' : serializer.data})
    
    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        
        try:
            instance = Women.objects.get(id=pk)
        except:
            return Response({'error': 'Object does not exist'})
        
        serializer = WomenSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'post' : serializer.data})
    
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error' : 'Method DELETE not allowed'})
        
        try:
            woman = Women.objects.get(pk=pk)
            woman.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Women.DoesNotExist:
            return Response({'error' : 'Obejct does not exist'}, status=status.HTTP_404_NOT_FOUND)

# class WomenAPIView(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
