from rest_framework import serializers
from .models import *
from examcontroller.models import *


class Branchserializer(serializers.ModelSerializer):
    class Meta:
        model=Branch
        fields=['id','branchname']
class Semesterserializer(serializers.ModelSerializer):
    class Meta:
        model=Semester
        fields=['id','semestername']
class Examserializer(serializers.ModelSerializer):
    class Meta:
        model=ExamDetails
        fields=['exam_name','exam_subject','exam_date','exam_time']
class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model=Studentprofile
        fields=['user','registerno','branch','semester']

class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields ='__all__'
class Subjectserializer(serializers.ModelSerializer):
    class Meta:
        model= Subject
        fields ='__all__'
class Classroomserializer(serializers.ModelSerializer):
    branch=serializers.CharField(source='subject.branch.branchname')
    semester=serializers.CharField(source='subject.semester')
    subjectname=serializers.CharField(source='subject.subjectname')
    subjectcode=serializers.CharField(source='subject.subjectcode')
    # c=Examdetails.objects.filter(exam_subject.subjectname=subjectname).first()

    class Meta:
        model=Seatingarrangement
        fields=['classroom_number','subject','seat_number','register_no','branch',
                'semester','subjectname','subjectcode']
# class TeacherseatingarrangementSerializer(serializers.ModelSerializer):
#
#     exam.
#         exam_hall
#     class Meta:
#         model=Teacherseatingarrangement
#         fields['exam',exam_hall,]
class Viewassignedclassserializer(serializers.ModelSerializer):
    examname=serializers.CharField(source='exam.exam_name')
    examdate=serializers.CharField(source='exam.exam_date')
    examtime=serializers.CharField(source='exam.exam_time')
    roomnumber=serializers.CharField(source='exam_hall.hallno')
    class Meta:
        model=Teacherseatingarrangement
        fields=['examname','examdate','examtime','roomnumber']
class Viewstaffprofileserializer(serializers.ModelSerializer):
    branchname=serializers.CharField(source='subject.branch.branchname')
    email=serializers.CharField(source='user.email')
    name=serializers.CharField(source='user.first_name')
    class Meta:
        model=Staffprofile
        fields=['name','email','staff_id','branchname']