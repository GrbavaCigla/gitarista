from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CurrentUserDefault,
)
from api.models import Sheet


class SheetSerializer(ModelSerializer):
    publisher = PrimaryKeyRelatedField(read_only=True, default=CurrentUserDefault())

    class Meta:
        model = Sheet
        fields = "__all__"
        extra_kwargs = {"sheet": {"write_only": True}}


class UserSerializer(ModelSerializer):
    sheets = PrimaryKeyRelatedField(many=True, queryset=Sheet.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "sheets"]
