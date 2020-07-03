from django.urls import path


from todo.views import todo


urlpatterns = [
    path('a/', todo),
]
