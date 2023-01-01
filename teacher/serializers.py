from rest_framework import serializers
from .models import TeacherInfo

class TeacherInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=TeacherInfo
        fields='__all__'

class TeacherUploadSerializer(serializers.ModelSerializer):
    # files=serializers.FileField()
    class Meta:
        model=TeacherInfo
        fields=['file']

class GradeSerializer(serializers.ModelSerializer):
    grade=serializers.IntegerField()

class TaskSerializer(serializers.ModelSerializer):
    grade=serializers.CharField(max_length=250)



