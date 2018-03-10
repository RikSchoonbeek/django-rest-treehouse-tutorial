from django.db import models


class TodoList(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class TodoListItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    todolist = models.ForeignKey(TodoList,
                                 on_delete=models.CASCADE)

    def __str__(self):
        return self.name
