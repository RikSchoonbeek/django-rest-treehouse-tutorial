from rest_framework import status  # For sending back status codes
from rest_framework.views import APIView
from rest_framework.response import Response

from . import models
from . import serializers


class ListCreateTodoList(APIView):
    def get(self, request, format=None): # format controls the format that comes back out
        todolists = models.TodoList.objects.all()
        serializer = serializers.TodoListSerializer(todolists, many=True)
        # many=True because we are serializing multiple objects
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.TodoListSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # If data is not valid, view stops and exception is raised
        serializer.save()  # Saves instance to database, but also updates serializer with 'id' field
        return Response(serializer.data, status=status.HTTP_201_CREATED)