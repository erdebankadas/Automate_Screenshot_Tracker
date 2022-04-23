"""""
from email.policy import default
#from typing_extensions import Required
from django.db import models
from django.conf import settings
#from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    assigned_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_assigned_by',
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='project_assigned_to',
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.title
        
class Contact(models.Model):
    full_name = models.CharField(max_length=30)
    relationship = models.CharField(max_length=30,default=None,null=True)
    email = models.EmailField(default=None,null=True)
    phone_number = models.CharField(max_length=10)
    #phone_number = PhoneNumberField(required=True, country='+91')
    another_number = models.CharField(max_length=10,default=None,null=True)
    #another_number = PhoneNumberField(required=True, country='+91')
     
    work_number = models.CharField(max_length=10,default=None,null=True)
    #work_number = PhoneNumberField(required=True,country='+91')
     
    office_number = models.CharField(max_length=10,default=None,null=True)
    #office_number = PhoneNumberField(required=True,country='+91')
     
    
    address = models.CharField(max_length=300,default=None,null=True)
    image = models.ImageField(upload_to='images/' ,default=None,null=True)

    def __str__(self):
          return self.full_name
          """""