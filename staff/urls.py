from django.contrib import admin

from django.urls import path,include
from .views import *

urlpatterns = [
    path('viewstudentsemandbranch/',Viewstudentsemandbranch.as_view(),name='viewstudentsemandbranch'),
    path('viewsemester/',Viewsemester.as_view(),name='viewsemester'),
    path('viewbranch/', Viewbranch.as_view(), name='viewbranch'),
    path('viewexams/<sem>/<branch>/<registerno>',Viewexam.as_view(),name='viewexam'),
    path('vewsubbranch/<sem>/<branch>',Viewsubjects.as_view()),#
    path('viewseat/<registerno>',Viewseat.as_view()),
    path('viewassignedclass/<id>',Viewassignedclass.as_view()),
    path('viewstaffprofile/<id>',Viewstaffprofile.as_view()),


    ]