from django.views.generic import ListView
from django.views.generic import DetailView


from todo.models import TodoModel


class TodoList(ListView):
    template_name = 'list.html'
    model = TodoModel


class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel
