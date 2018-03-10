from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.ListCreateTodoList.as_view(), name="list_list"),
    path('<int:pk>/',
         views.RetrieveUpdateDestroyTodoList.as_view(),
         name='list_detail'),
    path('<int:list_pk>/items/',
         views.ListCreateTodoListItem.as_view(),
         name="item_list"),
    path('<int:list_pk>/items/<int:item_pk>/',
         views.RetrieveUpdateDestroyTodoListItem.as_view(),
         name="item_detail")
]