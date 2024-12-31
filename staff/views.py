from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views import View
from examcontroller.models import Teacherseatingarrangement

# Create your views here.
class Viewstudentsemandbranch(APIView):
    def get(self,request,id):
        student_instances=Studentprofile.objects.filter(user=id).first()
        serializer=Studentserializer(student_instances,many=True)
        return Response(serializer.data)
class Viewsemester(APIView):
    def get(self,request):
        semester_instances=Semester.objects.all()
        serializer=Semesterserializer(semester_instances,many=True)
        return Response(serializer.data)
class Viewbranch(APIView):
    def get(self,request):
        semester_instances=Branch.objects.all()
        serializer=Branchserializer(semester_instances,many=True)
        return Response(serializer.data)
class Viewexam(APIView):
    def get(self,request):
        exam_instances=ExamDetails.objects.all()
        serializer=Examserializer(exam_instances,many=True)
        return Response(serializer.data)
class Viewsubjects(APIView):
    def get(self,request,sem,branch):
        subject_instances=Subject.objects.filter(branch=branch,semester=sem).all()
        serializer=Subjectserializer(subject_instances,many=True)
        return Response(serializer.data)
class Viewexam(APIView):
    def get(self,request,sem,branch,registerno):
        classroom_instances = Seatingarrangement.objects.filter(subject__semester=sem, subject__branch=branch,register_no=registerno).all().order_by('-exam_date')
        print(classroom_instances)
        serializer=Classroomserializer(classroom_instances,many=True)
        serialized_data_with_exam_details = []

        for data in serializer.data:
            print(data)
            exam_instances = ExamDetails.objects.filter(exam_subject=data['subject']).first()
            serialized_data_with_exam_details.append({
                'subject': data['subject'],
                'exam_name':exam_instances.exam_name,
                'exam_date': exam_instances.exam_date,
                'exam_time': exam_instances.exam_time,
                'subjectname':data['subjectname'],
                'classroom_number':data['classroom_number'],
                'subjectcode':data['subjectcode'],
                'register_no':data['register_no'],
                'branch':data['branch'],
                'seat_number':data['seat_number']

                # Include other fields from serializer.data if needed
            })

        return Response(serialized_data_with_exam_details)
class Viewseat(APIView):
    def get(self,request,registerno):
        seating_instances=Seatingarrangement.objects.filter(registerno=register_no).first()
        serializer=Seatingserializer(seating_instances,many=True)
        return Response(serializer.data)
# class TeacherSeatingArrangementView(APIView):
#     def get(self, request, teacher_id):
#         teacher_seating_arrangements = Teacherseatingarrangement.objects.filter(teacher_id=teacher_id)
#         serializer = TeacherseatingarrangementSerializer(teacher_seating_arrangements, many=True)
#         return Response(serializer.data)
class Viewassignedclass(APIView):
    def get(self,request,id):
        user_id=Userprofile.objects.get(pk=id)
        st_in=Teacherseatingarrangement.objects.filter(teacher=user_id).all()
        serializer=Viewassignedclassserializer(st_in,many=True)
        return Response(serializer.data)
class Viewstaffprofile(APIView):
    def get(self, request, id):
        user_id = Userprofile.objects.get(pk=id)
        st_in = Staffprofile.objects.filter(user=user_id).first()
        serializer = Viewstaffprofileserializer(st_in)
        return Response(serializer.data)