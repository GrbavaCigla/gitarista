from django.http import FileResponse, Http404
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from api.models import Sheet
from api.serializers import SheetSerializer
from api.permissions import IsPublisherOrReadOnly


class SheetDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsPublisherOrReadOnly]
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer


class SheetList(CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly, IsPublisherOrReadOnly]
    queryset = Sheet.objects.all()
    serializer_class = SheetSerializer

    def perform_create(self, serializer):
        serializer.save(publisher=self.request.user)


class SheetDownload(APIView):
    def get_object(self, pk):
        try:
            return Sheet.objects.get(pk=pk)
        except Sheet.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        sheet = Sheet.objects.get(pk=pk)

        return FileResponse(sheet.sheet)
