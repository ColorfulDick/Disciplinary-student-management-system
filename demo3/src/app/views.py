# -*- coding:utf-8 -*-
from django.shortcuts import render
from app.models import Students
# Create your views here.
def user_list(request):
    users = Students.objects.all()  #将User表中的所有对象赋值给users这个变量，它是一个列表
    return render(request, 'home.html', {'users': users})#生成一个user变量，这个变量可以给templates中的html文件使用
