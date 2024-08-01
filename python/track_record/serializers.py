from rest_framework import serializers
from . models import Track_record


class Track_record_serializer(serializers.ModelSerializer):
    class Meta :
        fields = '__all__'
        model = Track_record