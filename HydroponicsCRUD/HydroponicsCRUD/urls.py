"""
URL configuration for HydroponicsCRUD project.

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
from hydroponic_system.views import HydroponicSystemList, HydroponicSystemDetail
from measures.views import MeasureListCreate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('user_authentication.urls')),
    path('api/hydroponic-systems/', HydroponicSystemList.as_view()),
    path('api/hydroponic-systems/<int:pk>/', HydroponicSystemDetail.as_view()),
    path('api/measures/', MeasureListCreate.as_view()),
]
