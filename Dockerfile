FROM python:latest
RUN apt-get update
RUN pip install --upgrade pip
COPY requirements.txt /app/requirements.txt

WORKDIR /app

# RUN pip install -r requirements.txt
