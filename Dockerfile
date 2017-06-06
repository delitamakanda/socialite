FROM debian:latest

ENV DEBIAN_FRONTEND noninteractive

ADD hello /opt/hello
ADD requirements.txt /opt/hello/requirements.txt

RUN apt-get update && \
    apt-get install -y apt-utils

RUN apt-get install -y python python-pip && \
    pip install -r /opt/hello/requirements.txt


CMD python /opt/hello/hello.py
