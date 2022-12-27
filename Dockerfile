FROM python:3.11 as base
ENV PYTHONBUFFERED=1

WORKDIR /gotya
#FROM alphine
#RUN apk add --no-cache mariadb-connector-c-dev
#RUN apk update 
#RUN apk add python3 python3-dev mariadb-dev build-base 
#RUN pip3 install mysqlclient && apk del python3-dev mariadb-dev build-base
#RUN apk add netcat-openbsd

COPY requirements.txt requirements.txt
RUN pip install psycopg2
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]