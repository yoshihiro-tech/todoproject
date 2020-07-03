from django.urls import path


from todo.views import TodoList
from todo.views import TodoDetail


urlpatterns = [
    path('list/', TodoList.as_view()),
    path('detail/<int:pk>', TodoDetail.as_view())
]
