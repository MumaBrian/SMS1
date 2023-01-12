from rest_framework import serializers
from .models import SubjectInfo
class SubjectInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectInfo
        fields=['title','teacher','student','classroom']