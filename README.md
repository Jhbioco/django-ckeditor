# django-ckeditor
This project shows how to use ckeditor in django framework. 

**1. Create and activate virtualenv**
```
  virtualenv venv
  ```
  * _**source** venv/bin/activate_

**2. Install django on virtualenv**
  ```
  pip install django
  ```
  
**3. Install pillow**
```
  pip install pillow
 ````
 
**4. Create django project**
  ```
  django-admin startproject myproject
  ```
  
**5. Inside myproject folder, create django app**
  ```
  python manage.py startapp myapp
  ```
  
**6. Create super user**
  ````
   python manage.py createsuperuser
 ````
  
**7. Install django-ckeditor**
 ```
  pip install django-ckeditor
 ```
 
**8. Collect static files**
 ```
  python manage.py collectstatic
 ```
  
**9. Configure myproject/settings.py**

#
I marked the changes with red color.

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/settings.jpeg" width="300" height="300"/>

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/root.png" width=35% height=35%/>

**10. myproject/urls.py**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/urls.png" width=50% height=50%/>

**11. myapp/models.py**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/models.png" width=50% height=50%/>

**12. myapp/admin.py**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/admin.png" width=35% height=35%/>

**13. Django Admin**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/admin_myapp.png" width=50% height=50%/>

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/content.png" width=70% height=70%/>

For more information visit: https://django-ckeditor.readthedocs.io/en/latest/#django-ckeditor

