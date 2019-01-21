# FROM 758491395512.dkr.ecr.us-west-2.amazonaws.com/sie/roadster/develop/common/base-image/centos:6.8-master
FROM amazonlinux:latest

ENV HTTPS_PROXY=http://proxy.aws.infr.rs.scei.sony.co.jp:8080
ENV HTTPS_PROXY=http://proxy.aws.infr.rs.scei.sony.co.jp:8080

RUN yum update -y && yum install -y python3-devel python3-pip

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade -r requirements.txt

EXPOSE 5000
CMD python3 app.py