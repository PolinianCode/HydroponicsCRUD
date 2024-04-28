from rest_framework import generics, permissions
from .models import Measures
from hydroponic_system.models import HydroponicSystem
from .serializer import MeasurementSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):

    """
    Custom pagination class
    """

    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000


class MeasureListCreate(generics.ListCreateAPIView):
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = Pagination

    def get_queryset(self):
        """
        Get the measures for the current user
        With additional filtering options
        """

        queryset = Measures.objects.filter(
            hydroponic_system__owner=self.request.user)
        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            queryset = queryset.filter(time__range=[start_date, end_date])

        sort_by = self.request.query_params.get('sort_by', None)

        if sort_by:
            queryset = queryset.order_by(sort_by)
        return queryset

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


class LastMeasurements(generics.ListAPIView):
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = Pagination

    def get_queryset(self):
        system_id = self.kwargs['system_id']
        queryset = Measures.objects.filter(hydroponic_system__id=system_id)
        queryset = queryset.order_by('-time')[:10]
        return queryset


class MeasurementList(generics.ListAPIView):
    queryset = Measures.objects.all()
    serializer_class = MeasurementSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = Pagination

    def get_queryset(self):
        """

        Get all the measures with additional filtering options and sorting

        """

        queryset = Measures.objects.all()

        start_date = self.request.query_params.get('start_date', None)
        end_date = self.request.query_params.get('end_date', None)
        if start_date and end_date:
            if start_date > end_date:
                return Response({"error": "Incorrect time range"}, status=status.HTTP_400_BAD_REQUEST)
            queryset = queryset.filter(
                time__gte=start_date, time__lte=end_date)

        sort_by = self.request.query_params.get('sort_by', None)
        if sort_by:
            queryset = queryset.order_by(sort_by)

        return queryset
