from django.shortcuts import render


from rest_framework.generics import ListAPIView, CreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import OrderingFilter

from .models import Todolist_model
from .serializers import todolist_serializers


class todo_create_view(CreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class= todolist_serializers
    queryset=Todolist_model.objects.all()

class todo_list_view(ListAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class= todolist_serializers
    filter_backends=(OrderingFilter)
    ordering_fields=['name','creation_date']

    def get_queryset(self):
        """
        This view should return a list of all the todolist
        for the currently authenticated user.
        """
        user = self.request.user
        return Todolist_model.objects.filter(user=user)

class todo_retrieveupdatedelete_view(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class= todolist_serializers
    lookup_field='id'
    queryset=Todolist_model.objects.all()