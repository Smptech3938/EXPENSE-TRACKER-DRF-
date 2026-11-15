from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Expense
        fields="__all__"
        read_only_fields=["created_at","id","owner"]

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","password","email"]
        extra_kwargs={
            "password":{"write_only":True}
        }

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)
    