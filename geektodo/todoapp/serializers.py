from rest_framework import serializers
from .models import Project
from .models import ToDo


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ToDo
        fields = '__all__'
