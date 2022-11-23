"""District URL Configuration

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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage,name="Homepage"),
    path('admin-login-portal/', views.adminloginportal,name="AdminLoginPortal"),
    path('admin-portal/', views.adminportal,name="AdminPortal"),
    path('insert-citizen/', views.InsertCitizen,name="InsertCitizen"),
    path('citizen-details/', views.showallcitizen,name="CitizenDetails"),
    path('citizen-login-portal/', views.citizenloginportal,name="CitizenLoginPortal"),
    path('citizen-portal/', views.citizenportal,name="CitizenPortal"),
    path('citizen-complaint-portal/', views.citizencomplaintportal,name="CitizenComplaintPortal"),
    path('tehsildar-login-portal/', views.tehsildarloginportal,name="TehsildarLoginPortal"),
    path('tehsildar-portal/', views.tehsildarportal,name="TehsildarPortal"),
    path('tehsildar-complaints-portal/', views.tehsildarcomplaintsportal,name="TehsildarComplaintsPortal"),
    path('solved-complaints/', views.runQuerySolvedComplaints,name="SolvedComplaints"),
    path('status-complaints/', views.runQueryStatusComplaints,name="StatusComplaints"),
    path('sdo-login-portal/', views.sdologinportal,name="SDOLoginPortal"),
    path('sdo-portal/', views.sdoportal,name="SDOPortal"),
    path('tehsil-tehsildar-details/', views.runQueryTehsilTehsildar,name="TehsilTehsildarDetails"),
    path('about-us/', views.aboutus,name="AboutUs"),
]
