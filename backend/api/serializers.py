from rest_framework import serializers
from api.models import Sheet
from django.contrib.auth.models import User


class SheetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sheet
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    sheets = serializers.PrimaryKeyRelatedField(many=True, queryset=Sheet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'sheets']