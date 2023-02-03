"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

# Import static
from django.conf.urls.static import static

# Import settings
from django.conf import settings

# Import Service view
from app.views import ServiceView

# Import route
from rest_framework import routers

# Create route instance to handle api routing
route = routers.DefaultRouter()
route.register('', ServiceView, basename='services')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(route.urls)),
]

# Media redirection using static configurations
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)