from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.
from .serializers import *
from .models import *
from rest_framework import status


class PersonView(APIView):
    def post(self,request):
        self.data=self.request.data
        serializer=PersonSerializer(data=self.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request):
        self.data=self.request.data
        person=Person.objects.all()
        serializer=PersonSerializer(person,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
 
class PersonViewUpdate(APIView):

    def patch(self,request,pk):
        self.data=self.request.data
        person=Person.objects.get(pk=pk)
        serializer=PersonSerializer(person,data=self.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def put(self,request,pk):
        self.data=self.request.data
        person=Person.objects.get(pk=pk)
        serializer=PersonSerializer(person,data=self.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,pk):
        person=Person.objects.get(pk=pk)
        serializer=PersonSerializer(person)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def delete(self,request,pk):
        person=Person.objects.get(pk=pk)
        person.delete()
        return Response({'msg':'deleted'},status=status.HTTP_200_OK)