from django.urls import path

from adminn import views
urlpatterns = [
    path('student/',views.Student.as_view()),
    path('student-details/<int:pk>/',views.StudentInfoDetails.as_view()),
    path('class/',views.ClassInfoView.as_view()),
    path('class-details/<int:pk>/',views.ClassInfoDetails.as_view()),
    path('subject/',views.SubjectInfoView.as_view()),
    path('subject-details/<int:pk>/',views.SubjectInfoDetails.as_view()),
    path('teacher/',views.TeacherInfoView.as_view()),
    path('teacher-details/<int:pk>/',views.TeacherInfoDetails.as_view()),
    path('parent/',views.ParentInfoView.as_view()),
    path('parent-details/<int:pk>/',views.ParentInfoDetails.as_view()),
    path('teacher-upload/',views.TeacherFileUploadView.as_view()),

]

