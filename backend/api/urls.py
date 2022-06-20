from django.contrib import admin
from django.urls import path, include

from api.views import SheetDetails

urlpatterns = [
    path('sheets/<int:pk>/', SheetDetails.as_view())
]
