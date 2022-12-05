FROM python:3.10.2 as base
ENV PYTHONBUFFERED=1

WORKDIR /gotya

COPY requirements.txt requirements.txt
RUN pip install django-environ
RUN pip install django-crispy-forms
RUN pip install crispy-bootstrap5
RUN pip install -r requirements.txt

COPY . .
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]