# django-blog
【项目目录】  
wsgi.py python应用与web服务器之间的接口  
urls.py URL配置文件  
settings.py 项目总配置文件  
_init_.py python中声明模块的文件 

【应用目录】  
migrations 数据移植（迁移）模块  
admin.py 该应用的后台管理系统  
apps.py  
models.py 数据模块  
tests.py 自动化测试模块  
views.py 执行响应的代码所在模块  

ORM 对象关系映射  
django-admin startproject myblog  
python manage.py startapp blog  
python manage.py makemigrations  
python manage.py migrate  
python manage.py sqlmigrate blog 0001  
python manage.py createsuperuser  
