# django-ckeditor
This project shows how to use ckeditor in django framework. 

**1. Create and activate virtualenv**

  * _**virtualenv** venv_

  * _**source** venv/bin/activate_

**2. Install django on virtualenv**
  * _**pip install** django_
  
**3. Install pillow**
  * _**pip install** pillow_
  
**4. Create django project**
  * _**django-admin startproject** myproject_
  
**5. Inside myproject folder, create django app**
  * _**python manage.py startapp** myapp_
  
**6. Create super user**
  *. _**python manage.py** createsuperuser_
  
**7. Install django-ckeditor**
  *. _**pip install** django-ckeditor_
  
**8. Collect static files**
  *. _**python manage.py** collectstatic_
  
**9. Configure myproject/settings.py**

I marked the changes with red color.

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/settings.jpeg" width="300" height="300"/>

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/root.png" width=50% height=50%/>

**10. myproject/urls.py**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/urls.png" width=50% height=50%/>

**11. myapp/models.py**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/models.png" width=50% height=50%/>

**12. myapp/admin.py**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/admin.png" width=35% height=35%/>

**13. Django Admin**

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/admin_myapp.png" width=50% height=50%/>

<img src ="https://github.com/Jhbioco/django-ckeditor/blob/master/myproject/media/uploads/2019/02/23/content.png" width=70% height=70%/>

