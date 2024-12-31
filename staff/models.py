from django.db import models
from user.models import Userprofile
from examcontroller.models import Semester
# Create your models here.
class Staffprofile(models.Model):
    user=models.OneToOneField(Userprofile,null=True,blank=True,on_delete=models.CASCADE)
    staff_no=models.CharField(max_length=40,null=True,blank=True)
    subject=models.ForeignKey(Semester,null=True,blank=True,on_delete=models.CASCADE)

