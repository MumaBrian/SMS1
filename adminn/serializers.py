from rest_framework.serializers import Serializer,FileField
from .models import TaskUpload
class UploadSerializer(Serializer):
    
    models=TaskUpload
    fields=['file']