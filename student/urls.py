from django.urls import path,include
from student import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('pdf/',views.DownloadFileView.as_view()),
    path('',views.chatbot_view, name='chatbot'),
    
]


