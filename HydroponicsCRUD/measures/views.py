from rest_framework import generics, permissions
from .models import Measures
from hydroponic_system.models import HydroponicSystem
from .serializer import MeasurementSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MeasureListCreate(generics.ListCreateAPIView):
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = Pagination

    def get_queryset(self):
        return Measures.objects.filter(hydroponic_system__owner=self.request.user)

    def create_measure(self, request, *args, **kwargs):
        hydroponic_system_id = self.request.data['hydroponic_system']
        try:
            system = HydroponicSystem.objects.get(
                id=hydroponic_system_id)
        except HydroponicSystem.DoesNotExist:
            return Response({"error": "Hydroponic system doesnt exist"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(hydroponic_system=system)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
