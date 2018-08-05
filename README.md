如有疑问，可咨询作者QQ：1123063417

违纪学生信息管理系统（Disciplinary-student-management-system）
========
相关技术：python3.6、django2.0、xadmin2.0
------------

输入127.0.0.1:8000/admin可进入管理系统

输入127.0.0.1:8000/students可查看已经加入的违纪学生信息（html页面）

#实现功能：
----------

*注册了两个类模板，一个是“学生信息”，另一个是“班级信息”，班级信息为学生信息的外键

*学生信息能输入学生姓名，性别（可选男/女），班级（需要提前在“班级信息”一栏注册好），违纪日期，违纪原因，处分类型（可选警告、严重警告、记过、留校察看），相关照片（可以插入一张图片，插入保存以后方可查看）

*可以导出学生信息为excel（axdmin模板自带功能）

*可以查看、更改操作日志（例如哪个管理员删除谁，加入了谁。axdmin模板自带功能）

图片介绍：
------------
![image](https://github.com/ColorfulDick/Disciplinary-student-management-system/blob/master/360%E6%88%AA%E5%9B%BE-50447821.jpg)

![image](https://github.com/ColorfulDick/Disciplinary-student-management-system/blob/master/360%E6%88%AA%E5%9B%BE-50496712.jpg)

![image](https://github.com/ColorfulDick/Disciplinary-student-management-system/blob/master/360%E6%88%AA%E5%9B%BE-50522670.jpg)
