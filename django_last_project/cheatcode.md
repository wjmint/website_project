creating `venv`

- `venv` = Virtual Enviroment

```bash
python -m venv ./venv
```



Activate `venv` file	

```bash
source ./venv/Scripts/activate
```



Deactivate `venv` file

```bash
deactivate
```



Creating a Django project 

- `name` is the name of the project
- **optional** `location`, if you want to create it in current location, use `.` 

```bash
django-admin startproject `name` `location`
```



Checking all the libreries or packages that are installed in this `venv`

```bash
pip freeze
```



Creating an application inside Django project

- `name` is the name of the application

```bash
django-admin startapp `name`
```



Creating superuser(admin)

```bash
python manage.py creatsuperuser
```





Running the Django project

- If you are having an error when you run server for the first time than just install Django using `pip`

```bash
python manage.py runserver
```



We are going to use:

``from django.shortcuts import render``

only when  we have ``jinja`` template otherwise, we will use ``from django.http import HttpResponse`` to return raw `html`

```py
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = '<h1>Hello World</h1>'
    return HttpResponse(html)
```



Migrate

```bash
python manage.py makemigrations

//after

python manage.py migrate
```



## Postgresql

### Making new database

```sql
CREATE DATABASE `name` OWNER `owner_name`
```

