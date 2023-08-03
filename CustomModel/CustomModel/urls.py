"""
URL configuration for CustomModel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from auth_app.views import AddAPI
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh
from projects.views import ProjectDetailAPI, ProjectCreateAPI
from rest_framework.authtoken.views import obtain_auth_token
urlpatterns = [
    path('admin/', admin.site.urls),
     path('register/',AddAPI.as_view()),
     path('proj/', ProjectCreateAPI.as_view()),
     path('project/<int:pk>/', ProjectDetailAPI.as_view()),
     path("access/",token_obtain_pair ),
     path("refresh/",token_refresh),
     path('token/', obtain_auth_token),
]
