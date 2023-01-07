from django.urls import path
from student import views
urlpatterns = [
    path('',views.DownloadFileView.as_view()),
    path('number/',views.UserView.as_view()),
]