from django.contrib import admin
from django.urls import path, include

from api.views import SheetDetail, SheetList, SheetDownload

urlpatterns = [
    path('sheets/', SheetList.as_view(), name='sheet-list'),
    path('sheets/<int:pk>/', SheetDetail.as_view(), name='sheet-detail'),
    path('sheets/<int:pk>.musicxml', SheetDownload.as_view(), name='sheet-download'),
]
