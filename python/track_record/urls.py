from django.urls import path, include 
from . views import Track_record_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('activities',Track_record_views, basename= 'activities')



urlpatterns = [
    path('', include(router.urls))
]
