from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from django.contrib.auth.models import User
from .serializers import ExpenseSerializer,UserSerializer
from .models import Expense

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework import authentication,permissions

class CreateUserView(CreateAPIView):
    serializer_class=UserSerializer

class CreateExpenseView(CreateAPIView,ListAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    filter_backends=[
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields=["payment","category"]
    search_fields=["title"]
    ordering_fields=["amount","created_at"]

    def get_queryset(self):
        queryset=Expense.objects.filter(owner=self.request.user)
        return queryset

    def perform_create(self, serializer):
        user=self.request.user
        return serializer.save(owner=user)

class UpdateRetrieveDeleteView(UpdateAPIView,RetrieveAPIView,DestroyAPIView):
    serializer_class=ExpenseSerializer
    authentication_classes=[authentication.BasicAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    lookup_url_kwarg="id"

    def get_queryset(self):
        return Expense.objects.filter(owner=self.request.user)