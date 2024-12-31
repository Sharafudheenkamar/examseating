from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('', WebLogin.as_view(), name='weblogin'),
    path('userloginapi/', UserLoginapi.as_view(), name='userloginapi'),
    path('userlogout/',Logout.as_view(),name='userlogout'),
    path('userlogoutapiview',LogoutAPIView.as_view(),name='logoutapiview'),
    path('examcontrollerdashboard/',Examcontrollerdashboard.as_view(),name='admindashboard'),
    path('staffdashboard/',Staffdashboard.as_view(),name=''),

    path('studentregistration/', UserprofileCreateAPIView.as_view(), name='student_registration'),
    path('studentregistration/<int:pk>', UserprofileCreateAPIView.as_view(), name='student_registration_update'),
    path('teacheregistration/<int:pk>', TeacherprofileCreateAPIView.as_view(), name='staff_registration_update'),
    path('teacheregistration/', TeacherprofileCreateAPIView.as_view(), name='staff_registration_update'),
    # path()
]
