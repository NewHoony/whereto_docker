FROM python:3.8.0

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update

RUN mkdir -p /home/ec2-user/whereto

ADD . /home/ec2-user/whereto

WORKDIR /home/ec2-user/whereto

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python3 manage.py migrate
