from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views



router = DefaultRouter()
router.register('list', views.DoctorViewset)
router.register('designation', views.DesignationViewset)
router.register('specialization', views.SpecializationViewset)
router.register('availabletime', views.AvailableTimeViewset)
router.register('review', views.ReviewleViewset)

urlpatterns = [
    path('', include(router.urls))
]
