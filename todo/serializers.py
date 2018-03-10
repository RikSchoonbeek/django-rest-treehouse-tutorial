from rest_framework import serializers

from . import models


class TodoListSerializer(serializers.ModelSerializer):
        class Meta:
            fields = (
                'id',
                'description',
                'name'
            )
            model = models.TodoList


class TodoListItemSerializer(serializers.ModelSerializer):
        class Meta:
            fields = (
                'id',
                'description',
                'name'
            )
            model = models.TodoListItem
