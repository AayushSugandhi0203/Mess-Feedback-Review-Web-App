

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index, name='index'),
    path('index',views.index,name = 'index'),
    path('student',views.student,name = 'student'),
    path('adminpanel',views.adminpanel,name = 'adminpanel')
]
