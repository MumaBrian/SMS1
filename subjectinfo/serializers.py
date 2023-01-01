from rest_framework import serializers
from .models import StudentModel

class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['tile','teacher','student','classroom']