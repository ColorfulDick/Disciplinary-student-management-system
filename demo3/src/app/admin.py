# -*- coding:utf-8 -*-
#from django.contrib import admin

# Register your models here.
import xadmin
from app.models import Students,Class

class StudentsAdmin(object):
    list_display = ('name', 'sex', 'class_name','studentname','level',)
    search_fields = ('name','studentname',)
class ClassAdmin(object):
    list_display = ('class_name',)
    search_fields = ('class_name')

xadmin.site.register(Students, StudentsAdmin)
xadmin.site.register(Class, ClassAdmin)
xadmin.AdminSite.site_header ='违纪管理系统后台'
xadmin.AdminSite.site_title = '违纪管理系统'