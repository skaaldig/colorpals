from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from colors import views

router = routers.DefaultRouter()
router.register(r'images', views.ImageViewSet)
router.register(r'colors', views.ColorPaletteViewSet)

urlpatterns = [
    path('', views.color_input, name="color_input"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]