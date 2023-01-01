from django.urls import path
from  teacher import views
app_name = "teacher"
urlpatterns = [
    path('',views.TeacherFileUploadView.as_view()),
    path('excel/',views.DownloadFileView.as_view()),
    # path('', views.index, name='index'),
]