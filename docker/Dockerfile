FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y openjdk-19-jdk

RUN apt install -y python3
RUN apt -y install python3-pip
RUN pip install pygments

COPY ./python /python
ADD ./ApiClient-0.0.1-SNAPSHOT.jar /bin/
ADD ./config.json /resources/
CMD java -jar /bin/ApiClient-0.0.1-SNAPSHOT.jar --arg=/resources/config.json

EXPOSE 8080
