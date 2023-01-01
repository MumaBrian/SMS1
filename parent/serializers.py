from rest_framework import serializers
from .models import ParentInfo

class ParentSerializer(serializers.ModelSerializer):
    # image=serializers.ImageField()
    # contact=serializers.IntegerField()
    class Meta:
        model=ParentInfo
        fields=['name','child','address','contact','image']

