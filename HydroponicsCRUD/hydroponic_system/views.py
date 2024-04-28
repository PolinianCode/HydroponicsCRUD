from rest_framework import generics
from .models import HydroponicSystem
from .serializer import HydroponicSystemSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404


class HydroponicSystemList(generics.ListCreateAPIView):
    serializer_class = HydroponicSystemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    # Creating a new hydroponic system
    def perform_create(self, request):
        serializer = HydroponicSystemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HydroponicSystemDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HydroponicSystemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return HydroponicSystem.objects.filter(owner=self.request.user)

    # Deleting a hydroponic system
    def delete(self, request, *args, **kwargs):
        system = self.get_object()
        if system:
            self.perform_destroy(system)
            return Response({"message": "System has been deleted"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "System doesnt exist"}, status=status.HTTP_404_NOT_FOUND)

    # Updating a hydroponic system
    def perform_update(self, request, *args, **kwargs):
        system = self.get_object()
        user = request.user
        serializer = HydroponicSystemSerializer(
            system, owner=user, name=request.data.get('name'))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        obj = get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj
