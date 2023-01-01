from django.shortcuts import render
from rest_framework import generics,permissions
from classinfo.models import ClassInfo
from classinfo.serializers import ClassInfoSerializer
from parent.models import ParentInfo
from parent.serializers import ParentSerializer
from student.serializers import StudentSerializer,StudentUploadSerializer
from student.models import StudentModel
from subjectinfo.models import SubjectInfo
from subjectinfo.serializers import SubjectInfoSerializer
from teacher.models import TeacherInfo
from teacher.serializers import TeacherInfoSerializer,TeacherUploadSerializer
from .serializers import UploadSerializer
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from.models import TaskUpload  
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import (
    MultiPartParser,
    FormParser
)
import io
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from django_filters.rest_framework import DjangoFilterBackend
import pandas as pd


           

# Create your views here.

class Student(generics.ListCreateAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    permission_classes = [permissions.IsAdminUser]


class StudentInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer
    permission_classes = [permissions.IsAdminUser]




class ClassInfoView(generics.ListCreateAPIView):
    queryset=ClassInfo.objects.all()
    serializer_class=ClassInfoSerializer
    permission_classes = [permissions.IsAdminUser]


class ClassInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ClassInfo.objects.all()
    serializer_class=ClassInfoSerializer
    permission_classes = [permissions.IsAdminUser]

class SubjectInfoView(generics.ListCreateAPIView):
    queryset=SubjectInfo.objects.all()
    serializer_class=SubjectInfoSerializer
    permission_classes = [permissions.IsAdminUser]


class SubjectInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=SubjectInfo.objects.all()
    serializer_class=SubjectInfoSerializer
    permission_classes = [permissions.IsAdminUser]

class TeacherInfoView(generics.ListCreateAPIView):
    queryset=TeacherInfo.objects.all()
    serializer_class=TeacherInfoSerializer
    permission_classes = [permissions.IsAdminUser]


class TeacherInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=TeacherInfo.objects.all()
    serializer_class=TeacherInfoSerializer
    permission_classes = [permissions.IsAdminUser]

class ParentInfoView(generics.ListCreateAPIView):
    queryset=ParentInfo.objects.all()
    serializer_class=ParentSerializer
    permission_classes = [permissions.IsAdminUser]


class ParentInfoDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=ParentInfo.objects.all()
    serializer_class=ParentSerializer
    permission_classes = [permissions.IsAdminUser]



class TeacherFileUploadView(generics.GenericAPIView):
    serializer_class = TeacherUploadSerializer
    queryset=TeacherInfo.objects.all()
    
    # permission_classes = (,)
    parser_classes = (MultiPartParser, FormParser,)

    def post(self, request, *args, **kwargs):
        serializer = TeacherUploadSerializer(data=request.data)
        # request.data._mutable=True


        """Upload the CSV file.

        Then reads it and saves csv data to database.

        Endpoint: /api/patients/file_upload/
        """
        # request.data['owner'] = request.user

        # Commented code is for debugging only
        # import pdb; pdb.set_trace()
        # print(to_dict['_name'])
        _dict_file_obj = request.data['file'].__dict__

        _csv = _dict_file_obj['_name'].endswith('.csv')

        _excel = _dict_file_obj['_name'].endswith('.xlsx')

        if request.data['file'] is None:
            return Response({"error": "No File Found"},
                            status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            data = self.request.data.get('file')

            if _csv is True:
                data_set = data.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                io_string = io.StringIO(data_set)

                csv_file = pd.read_csv(io_string, low_memory=False)
                columns = list(csv_file.columns.values)

                first_name, last_name, address,email,contact,age= columns[0], columns[1],columns[2],columns[3],columns[4],columns[5]

                instances = [
                    TeacherInfo(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        contact=row[contact],
                        age=row[age],
                        address=row[address],
                        email=row[email]
                    )

                    for index, row in csv_file.iterrows()
                ]

                TeacherInfo.objects.bulk_create(instances)

            elif _excel is True:
                xl = pd.read_excel(data)
                columns = list(xl.columns.values)
                first_name, last_name, address,email,contact,age= columns[0], columns[1],columns[2],columns[3],columns[4],columns[5]
                instances = [
                    TeacherInfo(
                        firstname=row[first_name],
                        lastname=row[last_name],
                        contact=row[contact],
                        age=row[age],
                        address=row[address],
                        email=row[email]
                    )

                    for index, row in xl.iterrows()
                ]

                TeacherInfo.objects.bulk_create(instances)

            else:
                return Response(data={"err": "Must be *.xlsx or *.csv File."},
                                status=status.HTTP_400_BAD_REQUEST
                                )

            serializer.save()
            return Response(
                {"message": "Upload Successfull",
                 "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    