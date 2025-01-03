from django.urls import path
from .views import *
urlpatterns=[



    path('viewsub/', Viewsub.as_view()),
    path('addsub/', Addsub.as_view()),
    path('editsub/<id>',Editsub.as_view()),
    path('deletesub/<id>',Deletesub.as_view()),

    path('viewexam/',View_exam.as_view()),
    path('addexam/', Add_exam.as_view()),
    path('deleteexam/<id>', Deleteexam.as_view()),


    #classroom
    path('viewclassroom/', ViewClassroom.as_view()),
    path('addclassroom/', AddClassroom.as_view(), name='addclassroom'),
    path('fetch-subjects/', fetch_subjects, name='fetch_subjects'),
    path('deleteclassroom/<id>',Deleteclassroom.as_view(),name='deleteclassroom'),

    path('viewseat/',Viewseat.as_view(),name='viewseat'),
    path('newseat/',Allocateseat.as_view(),name='newseat'),
    path('get_students_count/<str:exam_date>/', get_students_count, name='get_students_count'),
    path('get_class_details/<str:classroomId>/', get_class_details, name='get_class_details'),

    path('viewsubjects/',SubjectAPIView.as_view(),name='viewsubjects'),

    path('allocatestaff/',Allocatestaff.as_view(),name='allocatesstaff'),
    path('allocateviewstaff/', Allocateviewstaff.as_view(), name='allocateviewstaff'),
    path('allocatedeletestaff/<id>', Allocatedeletestaff.as_view(), name='allocatedeletestaff'),

    path('exam-study-material/', ExamstudymaterialAPIView.as_view(), name='exam-study-material'),
    path('exam-study-material/<int:pk>/', ExamstudymaterialAPIView.as_view(), name='exam-study-material-detail'),

    path('viewstaff/', ViewStaff.as_view()),
    path('addstaff/', AddStaff.as_view(), name='addclassroom'),
    path('deletestaff/<id>', Deletestaff.as_view(), name='deleteclassroom'),
    path('get_exam_halls/', get_exam_halls, name='get_exam_halls'),
    path('seating_arrangement_view',seating_arrangement_view,name='seating_arrangement_view')



]
