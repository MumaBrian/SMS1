from django.shortcuts import render
from .serializers import StudentSerializer,UserSerializer
from rest_framework import generics
from .models import StudentModel
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView



# Create your views here.
class DownloadFileView(generics.ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'report.xlsx'

class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Phone number is valid, do something with it
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)