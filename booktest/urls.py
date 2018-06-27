#!usr/bin/python3
# -*- coding:utf-8 -*-

# @Site 
# @File urls.py
# @Software PyCharm

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
]
