FROM python:3.8.4-slim

RUN pip install asgiref==3.2.10 \
    Django==3.0.8 \
    django-extensions==3.0.3 \
    pytz==2020.1 \
    sqlparse==0.3.1 \
    attrs==19.3.0 \
    importlib-metadata==1.7.0 \
    more-itertools==8.4.0 \
    packaging==20.4 \
    pluggy==0.13.1 \
    py==1.9.0 \
    pyparsing==2.4.7 \
    pytest==5.4.3 \
    pytest-django==3.9.0 \
    six==1.15.0 \
    wcwidth==0.2.5 \
    zipp==3.1.0 

RUN mkdir /app/
COPY . /app/
WORKDIR /app/
RUN pip install -r requirements/local.txt

WORKDIR /app/homemaid/
RUN python manage.py migrate

CMD ["python", "manage.py", "runserver"]
