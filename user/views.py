from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate
from .models import *
from django.contrib import messages
from rest_framework.views import APIView
# from .views import *
import json
from django.shortcuts import render
from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import *
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

# Create your views here.
class WebLogin(View):
    templates_name = 'login.html'
    def get(self,request):
        return render(request,self.templates_name)

    def post(self, request):
        user_type = ""
        response_dict = {"success": False}
        landing_page_url = {
        "STAFF":"staffdashboard",
            "ADMIN":"admindashboard"
        }
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        authenticated = authenticate(username=username,password=password)
        try:
            user = Userprofile.objects.get(username=username)
            # print("hello")
        except Userprofile.DoesNotExist:
            response_dict[
                           "reason"
                         ] = "No account found for this username. Pleas signup."
            messages.error(request, response_dict["reason"])
        if not authenticated:
            # print("notauthenticated")
            response_dict["reason"] = "invalid credentials."
            messages.error(request, response_dict["reason"])
            return redirect(request.GET.get("from") or "userlogin")

        else:
            # print("hello")
            session_dict = {"real_user": authenticated.id}
            token, c = Token.objects.get_or_create(
                       user=user, defaults={"session_dict": json.dumps(session_dict)}
            )
        user_type = authenticated.user_type
        print(user_type)
        request.session["data"] = {
                        "user_id": user.id,
                        "user_type": user.user_type,
                        "token":token.key,
                        "username": user.username,
                        "status": user.is_active,

                      }
        print("hai")
        print("user")
        print("user_type")
        request.session["user"] = authenticated.username
        request.session["token"] = token.key
        request.session["status"] = user.is_active
        return redirect(landing_page_url[user_type])
        return redirect(request.GET.get("from") or contractor)

from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
class UserLoginapi(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = tuple()

    def get(self, request):
        response_dict = {"status": False}
        response_dict["logged_in"] = bool(request.user.is_authenticated)
        response_dict["status"] = True
        return Response(response_dict, HTTP_200_OK)

    def post(self, request):
        response_dict = {"status": False, "token": None, "redirect": False}
        password = request.data.get("password")
        username = request.data.get("username")
        print(username)
        print(password)
        try:
            t_user = Userprofile.objects.get(username=username)
        except Userprofile.DoesNotExist:
            response_dict["reason"] = "No account found for this username. Please signup."
            return Response(response_dict, HTTP_200_OK)

        # blocked_msg = "This account has been blocked. Please contact admin."
        # today = utc_today()
        authenticated = authenticate(username=t_user.username, password=password)
        if not authenticated:
            response_dict["reason"] = "Invalid credentials."
            return Response(response_dict, HTTP_200_OK)

        user = t_user
        print(user)
        if not user.is_active:
            response_dict["reason"] = "Your login is inactive! Please contact admin"
            return Response(response_dict, HTTP_200_OK)

        session_dict = {"real_user": authenticated.id}
        token, c = Token.objects.get_or_create(
            user=user, defaults={"session_dict": json.dumps(session_dict)}
        )
        login(request, user, "django.contrib.auth.backends.ModelBackend")
        if user.user_type=='STUDENT':
            student_instances=Studentprofile.objects.filter(user=user.id).first()
            response_dict["session_data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "name": user.first_name,
                "status": user.status,
                # "studentsubject":student_instances.subject,
                "studentbranch":student_instances.branch.id,
                "studentbranchname":student_instances.branch.branchname,
                "studentsemester":student_instances.semester.id,
                "studentsemestername":student_instances.semester.semestername,
                "registerno":student_instances.registerno
            }

        else:
            response_dict["session_data"] = {
                "user_id": user.id,
                "user_type": user.user_type,
                "token": token.key,
                "username": user.username,
                "name": user.first_name,
                "status": user.status,
            }


        response_dict["token"] = token.key
        response_dict["status"] = True
        return Response(response_dict, HTTP_200_OK)


class homeconstructiondashboard(View):
    def get(self,request):
        return render(request,'home.html')


class Examcontrollerdashboard(View):
    def get(self, request):
        return render(request, 'base.html')


class Staffdashboard(View):
    def get(self, request):
        return render(request, 'staffdashboard.html')

class Logout(View):
    def get(self,request):
        request.session["token"]=None
        request.session.flush()
        # print(request.session["token"])
        return redirect("weblogin")

class LogoutAPIView(APIView):
    def get(self, request):
        if 'token' in request.session:
            # Clear the token from the session
            request.session['token'] = None
            request.session.flush()
            return Response({"message": "Logged out successfully."}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "No session token found."}, status=status.HTTP_400_BAD_REQUEST)

from .models import *
class UserprofileCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request,pk=None):
        if pk is not None:
            try:
                student_profile = Studentprofile.objects.get(user=pk)
                serializer = StudentProfileserializersview(student_profile,context={'request': request})
                return Response(serializer.data)
            except Studentprofile.DoesNotExist:
                return Response({"error":"StudentProfile does not exist"},status=status.HTTP_404_NOT_FOUND)
        else:

            student_profile = Studentprofile.objects.all()
            serializer = StudentProfileserializersview(student_profile,many=True, context={'request': request})
            return Response(serializer.data)

    def post(self, request):
        student_serializer = StudentProfileserializers(data=request.data)
        # print(user_data)
        print(request.data)
        # print(client_serializer,'client_serializer')
        user_serializer=Userprofileserializers(data=request.data)
        # print(user_serializer,'user_serializer')
        student_valid = student_serializer.is_valid()
        user_valid = user_serializer.is_valid()

        if student_valid and user_valid:

            password = request.data['registerno']


            # Hash the password
            hashed_password = make_password(password)
            user = user_serializer.save(user_type="STUDENT",password=hashed_password)
            student_serializer.save(user=user)

            return Response(student_serializer.data, status=status.HTTP_201_CREATED)

        return Response({'student_errors': student_serializer.errors if not student_valid else None,
                         'user_errors': user_serializer.errors if not user_valid else None},
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            student_profile = StudentProfile.objects.get(user=pk)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

        student_serializer = StudentProfileserializers(instance=student_profile, data=request.data, partial=True)
        user_serializer = Userprofileserializers(instance=student_profile.user, data=request.data, partial=True)

        student_valid = student_serializer.is_valid()
        user_valid = user_serializer.is_valid()

        if student_valid and user_valid:
            student_serializer.save()
            user_serializer.save()

            return Response(student_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'client_errors': student_serializer.errors if not student_valid else None,
                             'user_errors': user_serializer.errors if not user_valid else None},
                            status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user_profile = Userprofile.objects.get(user=pk)
        except Userprofile.DoesNotExist:
            return Response({"error": "Student profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # Delete associated user profile
        user_profile.user.delete()

        # Now, delete the student profile
        user_profile.delete()

        return Response({"success": "Student profile and associated user profile deleted successfully"},
                        status=status.HTTP_204_NO_CONTENT)

class TeacherprofileCreateAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request,pk=None):
        if pk is not None:
            try:
                student_profile = Staffprofile.objects.get(user=pk)
                serializer = StaffProfileserializersview(student_profile,context={'request': request})
                return Response(serializer.data)
            except StudentProfile.DoesNotExist:
                return Response({"error":"Staff Profile does not exist"},status=status.HTTP_404_NOT_FOUND)
        else:
            student_profile = Staffprofile.objects.all()
            serializer = StaffProfileserializersview(student_profile,many=True, context={'request': request})
            return Response(serializer.data)

    def post(self, request):
        student_serializer = StudentProfileserializers(data=request.data)
        # print(user_data)
        print(request.data)
        # print(client_serializer,'client_serializer')
        user_serializer=Userprofileserializers(data=request.data)
        # print(user_serializer,'user_serializer')
        student_valid = student_serializer.is_valid()
        user_valid = user_serializer.is_valid()

        if student_valid and user_valid:

            password = request.data['registerno']

            # Send the password through email
            # send_mail(
            #     'Your New Account Password',
            #     f'Your password: {password}',
            #     'from@example.com',
            #     [request.data['email']],
            #     fail_silently=False,
            # )

            # Hash the password
            hashed_password = make_password(password)
            user = user_serializer.save(user_type="STUDENT",password=hashed_password)
            student_serializer.save(user=user)

            return Response(student_serializer.data, status=status.HTTP_201_CREATED)

        return Response({'student_errors': student_serializer.errors if not student_valid else None,
                         'user_errors': user_serializer.errors if not user_valid else None},
                        status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            student_profile = StudentProfile.objects.get(user=pk)
        except StudentProfile.DoesNotExist:
            return Response({"error": "Student profile does not exist"}, status=status.HTTP_404_NOT_FOUND)

        student_serializer = StudentProfileserializers(instance=student_profile, data=request.data, partial=True)
        user_serializer = Userprofileserializers(instance=student_profile.user, data=request.data, partial=True)

        student_valid = student_serializer.is_valid()
        user_valid = user_serializer.is_valid()

        if student_valid and user_valid:
            student_serializer.save()
            user_serializer.save()

            return Response(student_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'client_errors': student_serializer.errors if not student_valid else None,
                             'user_errors': user_serializer.errors if not user_valid else None},
                            status=status.HTTP_400_BAD_REQUEST)





