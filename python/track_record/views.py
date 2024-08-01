from django.shortcuts import render
from . models import Track_record
from . serializers import Track_record_serializer
from rest_framework.viewsets import ModelViewSet

class Track_record_views(ModelViewSet):
    queryset = Track_record.objects.all()
    serializer_class = Track_record_serializer