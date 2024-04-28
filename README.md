# HydroponicsCRUD

## Intstalling

Firstly you need to clone the repository to your computer using the command below.

```bash
git clone https://github.com/PolinianCode/HydroponicsCRUD
```

Next step create and activate virtual enviroment

```bash
python -m venv venv

Windows
venv/Script/activate.bat
```

Install all requirements for the project from **requiremens.txt** file

```bash
pip install -r requirements.txt
```


## Configuration of database parameters

To configure database connection parameters, navigate to settings.py file to this part of code

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'hydroponicdb',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

After successfull database connection, you need to make all migrations

```bash
python manage.py migrate
```


## Run server

```bash
python manage.py runserver
```

