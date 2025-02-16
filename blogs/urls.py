from django.contrib import admin
from django.urls import path
from . import views


app_name = 'blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:pk>/', views.blogDetails, name='blogDetails'),
    path('add/', views.addBlog, name='addBlog'),
]
