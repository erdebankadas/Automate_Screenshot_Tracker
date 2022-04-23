"""""
from rest_framework import routers
from .views import ContactViewSet

router = routers.DefaultRouter()
router.register(r'projects', ContactViewSet)
# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = router.urls"""

from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
   path('', views.home)
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)