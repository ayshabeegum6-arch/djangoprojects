"""
URL configuration for library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
app_name="books"
from books import views
urlpatterns = [
    path('',views.Home.as_view(),name="home"),
    path('viewbooks',views.Viewbooks.as_view(),name="viewbooks"),
    path('addbooks',views.Addbooks.as_view(),name="addbooks"),
    path('detail/<int:i>',views.Detail.as_view(),name="detail"),
    path('edit/<int:i>',views.Edit.as_view(),name="edit"),
    path('delete/<int:i>', views.Delete.as_view(), name="delete"),


]
