from rest_framework import serializers
from .models import StudentModel
import phonenumbers 
from django.core.exceptions import ValidationError


class StudentSerializer(serializers.ModelSerializer):
   
    class Meta:
        model=StudentModel
        fields='__all__'


class StudentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentModel
        fields=['firstname','lastname','email','admission_id','age','contact','address','current_class','gender','file']


from django.conf import settings
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

class PhoneNumberField(serializers.Field):
    def to_internal_value(self, data):
        try:
            phone_number = phonenumbers.parse(data)
        except phonenumbers.phonenumberutil.NumberParseException:
            raise ValidationError(_("Invalid phone number format"))

        return phone_number

class UserSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(required=True)

    class Meta:
        model = StudentModel
        fields = ['phone_number']


