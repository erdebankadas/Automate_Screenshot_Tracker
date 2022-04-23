"""""
from .models import Contact
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ContactSerializer


class ContactViewSet(viewsets.ModelViewSet):
    
    
    API endpoint that allows projects to be viewed or edited.
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticated]
    """
from django.shortcuts import render

# Create your views here.
import random
import pyautogui
from django.conf import settings
from django.contrib import messages

def home(request):
   if request.method == "POST":
      ss = pyautogui.screenshot()
      img = f'myimg{random.randint(1000,9999)}.png'
      ss.save(settings.MEDIA_ROOT/img)
      messages.success(request,'screenshot has been taken')
      return render(request,'home.html',{'img':img})
   return render(request,'home.html')