from rest_framework import serializers
from .models import *
from examcontroller.models import *

class Userprofileserializers(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['first_name','dob']
class StudentProfileserializers(serializers.ModelSerializer):
    class Meta:
        model = Studentprofile
        fields = ['registerno','branch','semester']
class StudentProfileserializersview(serializers.ModelSerializer):
    student_name=serializers.CharField(source='user.first_name')
    branch_name=serializers.CharField(source='branch.branchname')
    semester=serializers.CharField(source='semester.semestername')
    dob=serializers.CharField(source='user.dob')

    class Meta:
        model = Studentprofile
        fields = ['registerno','student_name','branch_name','semester','dob']
class StaffProfileserializersview(serializers.ModelSerializer):
    student_name=serializers.CharField(source='user.first_name')
    email=serializers.CharField(source='user.email')
    branch=serializers.CharField(source='branch.branchname')

    class Meta:
        model = Staffprofile
        fields = ['registerno','student_name','branch_name','semester']