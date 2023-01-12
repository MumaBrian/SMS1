from django.db import models
from classinfo.models import ClassInfo
from student.models import StudentModel

from teacher.models import TeacherInfo

# Create your models here.
    
class SubjectInfo(models.Model):
    title=models.CharField(max_length=20)
    teacher=models.ManyToManyField(TeacherInfo)
    student=models.ManyToManyField(StudentModel,related_name='subjectinfos')
    classroom=models.ForeignKey(ClassInfo,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title

