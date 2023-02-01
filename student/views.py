from django.shortcuts import render
from .serializers import StudentSerializer,UserSerializer
from rest_framework import generics
from .models import StudentModel
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import openai
from django.http import HttpResponse,JsonResponse
from django.views import View
from rest_framework import viewsets
from .models import Chatbot
from .serializers import ChatbotSerializer


openai.api_key='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'
def chatbot_response(prompt):
    openai.api_key = "your_api_key"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=2048,
        n =1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]
def chatbot_view(request):
    user_input = request.GET.get("user_input")
    chatbot_response = chatbot_response(user_input)
    return JsonResponse({"chatbot_response": chatbot_response})

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




