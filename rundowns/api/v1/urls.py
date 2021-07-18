from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import RundownViewSet

router = DefaultRouter()
router.register("rundown", RundownViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
