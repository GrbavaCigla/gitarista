from django.http import FileResponse, Http404
from music21.converter import ArchiveManager
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import Sheet
from api.serializers import SheetSerializer
from api.permissions import IsPublisherOrReadOnly

import music21


class SheetDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsPublisherOrReadOnly]
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class SheetList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsPublisherOrReadOnly]
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def perform_create(self, serializer):
        contents = serializer.validated_data["sheet"].read()
        # mxml = music21.converter.parseData(contents)
        am = ArchiveManager(contents)
        
        thumbnail = am.getData("musicxml.png")

        serializer.save(publisher=self.request.user, thumbnail=thumbnail)


class SheetDownload(APIView):
    def get_object(self, pk):
        try:
            return Sheet.objects.get(pk=pk)
        except Sheet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sheet = Sheet.objects.get(pk=pk)

        return FileResponse(sheet.sheet)
