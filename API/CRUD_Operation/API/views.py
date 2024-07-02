from django.shortcuts import render
from .models import * 
from .serializer import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.

# Book View

@api_view(['GET'])
def getall(request):
    if request.method=='GET':
        bdata=Book.objects.all()
        serial=bookserializer(bdata,many=True)
        return Response(serial.data,status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def getid(request,id):
    try:
        bid=Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serial=bookserializer(bid)
    return Response(serial.data,status=status.HTTP_200_OK)

@api_view(['DELETE','GET'])
def deleteid(request, id):
    try:
        bid = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serial=bookserializer(bid)
        return Response(serial.data,status=status.HTTP_200_OK)
    
    if request.method == 'DELETE':
        bid.delete()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def savedata(request):
    if request.method == 'POST':
        serial=bookserializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT','GET'])
def updateid(request,id):
    try:
        bid = Book.objects.get(id=id)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method=='GET':
        serial = bookserializer(bid)
        return Response(serial.data,status=status.HTTP_200_OK)
    if request.method=='PUT':
        serial=bookserializer(data=request.data,instance=bid)
        if serial.is_valid():
            serial.save() 
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)