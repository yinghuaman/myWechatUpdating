## 系统名称：myWechatUpdating

```
    在这个项目中，用户可以上传动态，上传的内容包括文字和图片，也可以查看该动态的所有动态并分页展示，或者找到具体的动态进行查看、删除和更新。
```
***
#### 上手指南

```
    以下指南将帮助你在本地机器上安装和运行该项目，进行开发和测试。关于如何将该项目部署到在线环境，请参考部署小节。 
```

#### 依赖软件环境和库

```
硬件：Windows

软件：PyCharm、MySQL Server 8.0、python 3.5

库：Django 1.11.4==》pip install django==1.11.4
    rest_framework ==>pip install djangorestframework
    pyMysql==>pip install pyMysql
```

#### 系统文件目录

```python
│  manage.py                  #工程自带文件
│  README.md                  #指南
│  user.sql                   #用户表创建语句和数据文件
│  wechatupdate.sql           #动态表创建语句和数据文件
│  
├─.idea
│      
├─myWeChatUpdate
│  │  admin.py
│  │  apps.py
│  │  models.py               #创建的模型
│  │  serializers.py          #将查询到的结果进行序列化
│  │  tests.py
│  │  urls.py                 #视图路由
│  │  views.py                #所有在浏览器上显示的视图
│  │  __init__.py
│  │  
│  ├─migrations              #与数据库关联的迁移文件
│  │  │  0001_initial.py 
│  │  │  0002_user.py
│  │  │  __init__.py
│          
├─static                     #用户上传的图片文件
│  └─img
│                  
└─weChatUpdate
    │  settings.py
    │  urls.py
    │  wsgi.py
    │  __init__.py
```

#### 使用方法

1. 在cmd中切换到本系统文件manage.py所在目录，执行python manage.py runserver ["host":"port"]，可以不输，默认为本地服务器；
2. 在浏览器输入host:port/api/upfile，在此页面即可上传动态和查看所有动态；
3. 在浏览器输入host:port/api/upfile/[number]，输入要查看的动态的id，即可在此页面进行查看、更新和删除；




