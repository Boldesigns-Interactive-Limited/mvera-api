FROM python:3.7-alpine
MAINTAINER Boldesigns Interactive Limited

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./src /app

RUN adduser -D user
USER user

