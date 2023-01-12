from django.urls import path
from  teacher import views

urlpatterns = [
    path('',views.TeacherFileUploadView.as_view()),
    path('excel/',views.DownloadFileView.as_view()),
    
]