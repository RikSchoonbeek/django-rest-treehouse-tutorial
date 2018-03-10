from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.ListCreateTodoList.as_view(), name="list_todolists"),
]