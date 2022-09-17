from django.contrib.auth.models import User
from rest_framework.serializers import (
    ModelSerializer,
    PrimaryKeyRelatedField,
    CurrentUserDefault,
    HyperlinkedIdentityField,
    ReadOnlyField
)
from api.models import Sheet


class SheetSerializer(ModelSerializer):
    publisher = ReadOnlyField(source='publisher.username', default=CurrentUserDefault())
    sheet_url = HyperlinkedIdentityField(view_name='sheet-download')

    class Meta:
        model = Sheet
        fields = "__all__"
        extra_kwargs = {"sheet": {"write_only": True}}


class UserSerializer(ModelSerializer):
    sheets = PrimaryKeyRelatedField(many=True, queryset=Sheet.objects.all())

    class Meta:
        model = User
        fields = ["id", "username", "sheets"]
