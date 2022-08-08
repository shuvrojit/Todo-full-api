from rest_framework.generics import ListAPIView, RetrieveAPIView

from .models import Todo
from .serializers import TodoSerializer

class ListTodoView(ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailTodoView(RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
