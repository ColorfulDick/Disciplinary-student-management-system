# -*- coding:utf-8 -*-
from django.db import models
import os
# Create your models here.
class Class(models.Model):
    class_name = models.CharField(verbose_name='班级', max_length=100)
    
    class Meta:
        verbose_name = '班级'
        verbose_name_plural = '班级'

    def __str__(self):
        return self.class_name
    
class Students(models.Model):
    SEX=(
        ('男', '男'),
        ('女', '女'),
        )
    PUNISH=(
        ('警告','警告'),
        ('严重警告','严重警告'),
        ('记过','记过'),
        ('留校察看','留校察看'),
        )
    name = models.CharField(verbose_name='学生姓名', max_length=50)
    sex = models.CharField(verbose_name='性别',choices=SEX,max_length=50)
    class_name = models.ForeignKey(Class,verbose_name='所在班级', on_delete=models.CASCADE)
    studentname = models.CharField(verbose_name='学号', max_length=250, blank=True)
    enter_date = models.DateField(verbose_name='违纪时间')
    reason = models.TextField(verbose_name='违纪原因', blank=True)
    level=models.CharField(max_length=30,choices=PUNISH,verbose_name='处分类型')
    def get_photo(self, filename):
        return os.path.join('photo', '%s_%s_%s_%s' % (self.class_name, self.name, self.id, os.path.splitext(filename)[1]))
    photo = models.ImageField(verbose_name='相关照片', upload_to=get_photo, blank=True, null=True)
    
    class Meta:
        verbose_name = '学生信息'
        verbose_name_plural = '学生信息'
    
    def __str__(self):
        return self.name