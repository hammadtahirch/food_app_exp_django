# pull official base image
FROM python:3.7-alpine

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -e; \
        apk add --no-cache --virtual .build-deps \
                gcc \
                libc-dev \
                linux-headers \
                mariadb-dev \
                python3-dev \
                postgresql-dev \
        ;

# install dependencies
RUN pip install --upgrade pip
RUN pip install mysqlclient
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt


# copy project
COPY . /usr/src/app/