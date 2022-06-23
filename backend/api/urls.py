from django.contrib import admin
from django.urls import path, include

from api.views import SheetDetails, SheetList, SheetDownload

urlpatterns = [
    path('sheets/<int:pk>/', SheetDetails.as_view()),
    path('sheets/', SheetList.as_view()),
    path('sheets/<int:pk>.musicxml', SheetDownload.as_view(), name='sheet-download'),
]
