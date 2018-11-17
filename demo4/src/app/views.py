# -*- coding:utf-8 -*-
from django.shortcuts import render
from app.models import Students
from django.http import HttpResponse
# Create your views here.
def search(request):
    if request.method=='GET':
        return render(request,'search.html')
    if request.method=='POST':
        number=request.POST['search']
        if Students.objects.filter(studentname=number).exists():
            users=Students.objects.filter(studentname=number)
            return render(request,'home.html',{'users':users})
        else:
            return HttpResponse('恭喜，您暂时没有违纪纪录')