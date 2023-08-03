from rest_framework import serializers
from .models import ProjectModel

class ProjectModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectModel
        fields='__all__'

    