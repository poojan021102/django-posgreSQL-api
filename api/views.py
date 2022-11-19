from rest_framework.response import Response
from .models import Destination
from .serializer import DestinationSerializer
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET','POST'])
def get_data(request):
    if request.method == "GET":
        des = Destination.objects.all()
        serializer = DestinationSerializer(des,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    if request.method == "POST":
        serializer = DestinationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_304_NOT_MODIFIED)

@api_view(['GET'])
def delete_data(request,id):
    d = Destination.objects.filter(id=id)
    if d:
        d.delete()
        return Response(status = status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def put_data(request,id):
    if request.method == "PUT":
        serializer = DestinationSerializer(Destination.objects.get(id=id),data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status=status.HTTP_204_NO_CONTENT)