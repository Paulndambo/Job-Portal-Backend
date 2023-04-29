from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = "__all__"

class JobWriterSerializer(serializers.Serializer):
    upload = serializers.CharField(max_length=255)