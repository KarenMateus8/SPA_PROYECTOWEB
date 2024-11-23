"""
URL configuration for SPA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app_vehiculo import views

router = routers.DefaultRouter()
router.register('vehiculo',views.VehiculoViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_vehiculo/', include('app_vehiculo.urls')), 
]

urlpatterns = [
    path('api/events/', views.get_events, name='get_events'),
    path('api/events/add/', views.add_event, name='add_event'),
    path('api/events/edit/', views.edit_event, name='edit_event'),
    path('api/events/delete/', views.delete_event, name='delete_event'),
]

