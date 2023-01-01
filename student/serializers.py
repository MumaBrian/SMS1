from rest_framework import serializers
from .models import StudentModel

class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=StudentModel
        fields='__all__'


class StudentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['firstname','lastname','email','admission_id','age','contact','address','current_class','gender','file']