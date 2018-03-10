from django.shortcuts import get_object_or_404
from rest_framework import generics

from . import models
from . import serializers


class ListCreateTodoList(generics.ListCreateAPIView):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer


class RetrieveUpdateDestroyTodoList(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoList.objects.all()
    serializer_class = serializers.TodoListSerializer


class ListCreateTodoListItem(generics.ListCreateAPIView):
    queryset = models.TodoListItem.objects.all()
    serializer_class = serializers.TodoListItemSerializer

    def get_queryset(self):
        """
        Determine correct queryset in order to get only items for the specific list.
        Without this, the method will return all items
        """
        return self.queryset.filter(todolist_id=self.kwargs.get('list_pk'))

    def perform_create(self, serializer):
        """
        Prevent user from giving a different pk when they create a new item
        perform_create is run when an object is being created by the view
        """
        todolist = get_object_or_404(
            models.TodoList, pk=self.kwargs.get('list_pk')
        )
        serializer.save(todolist=todolist)


class RetrieveUpdateDestroyTodoListItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TodoListItem.objects.all()
    serializer_class = serializers.TodoListItemSerializer

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            todolist_id=self.kwargs.get('list_pk'),
            pk=self.kwargs.get('pk')
        )
