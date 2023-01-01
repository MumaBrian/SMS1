from django.db import models
# from subjectinfo.models import SubjectInfo
# Create your models here.
class TeacherInfo(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    contact=models.IntegerField(null=True)
    age=models.IntegerField(null=True)
    address=models.CharField(max_length=30)
    employment_date=models.DateField(null=True) #created
    image=models.ImageField(upload_to='uploads/% Y/% m/% d/',blank=True,null=True)
    file=models.FileField(upload_to='media/%y/%m',null=True)
    email = models.CharField(max_length=250)


    def __str__(self):
        return " {}-{} ".format(self.firstname, self.lastname)

