# -*- coding:utf-8 -*-
from django.urls import path
from app.views import *

urlpatterns = [
    path(r'students',user_list),
]