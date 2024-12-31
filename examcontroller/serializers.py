from rest_framework import serializers
from .models import *
from user.models import Userprofile
class Studentprofileserializerview(serializers.ModelSerializer):
    student_name = serializers.CharField(source='user.first_name', read_only=True)
    student_dob = serializers.CharField(source='user.dob', read_only=True)
    student_branch = serializers.CharField(source='branchandsemester.semesterno', read_only=True)
    student_semester = serializers.CharField(source='branchandsemester.branch.branchname', read_only=True)

    class Meta:
        model = Studentprofile
        fields =['registerno','branch','semester','student_name','student_dob']
class Userprofieserializer(serializers.ModelSerializer):
    class Meta:
        model = Userprofile
        fields = ['dob','first_name']
class Studentprofileserializerpost(serializers.ModelSerializer):
    class Meta:
        model = Studentprofile
        fields = ['registerno','branchandsemester']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=Subject
        fields='__all__'