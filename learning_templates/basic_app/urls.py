# -*- coding: utf-8 -*-
from django.urls import path, include
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app'

urlpatterns = [
    path(r"relative/", views.relative, name='relative'),
    path(r"other/", views.other, name='other'),
    
    ]
