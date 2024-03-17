from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('order/',Orderview)


urlpatterns=[
    path('',include(router.urls))
]
