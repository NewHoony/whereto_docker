FROM python:3.8.0

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN mkdir -p /home/hoon/whereto

ADD . /home/hoon/whereto

WORKDIR /home/hoon/whereto

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
