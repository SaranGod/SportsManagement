"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from form_app.views import form_view,home_view

admin.site.site_header = "Sports Management System Admin "
admin.site.site_title = "Admin Page "

urlpatterns = [
    path("enter/list/",form_view),
    #path("enter/",form_enter),
    path('admin/', admin.site.urls),
    #path('', include('django.contrib.auth.urls'),  {'template_name': 'registration/login.html'}),
    #path('gameowner/', include('django.contrib.auth.urls'),  {'template_name': 'registration/login1.html'}),
    path('',home_view)
]
