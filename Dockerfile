FROM python:3.10.6 as base
ENV PYTHONBUFFERED=1

WORKDIR /gotya

RUN apk add --no-cache mariadb-connector-c-dev
RUN apk update && apk add python3 python3-dev mariadb-dev build-base && pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base

RUN apk add netcat-openbsd

COPY requirements.txt requirements.txt
RUN pip install django-environ
RUN pip install django-crispy-forms
RUN pip install crispy-bootstrap5
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]