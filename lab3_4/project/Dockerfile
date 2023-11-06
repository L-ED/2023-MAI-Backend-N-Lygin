FROM ubuntu:18.04
ADD . /app
RUN apt-get update
RUN apt-get install -y python3.8 python3-pip postgresql postgresql-contrib nginx
RUN pip3 install -r /app/requirements.txt
RUN cp ./nginx.conf /etc/nginx/nginx.conf
RUN 
USER nobody
WORKDIR /app
CMD /usr/local/bin/gunicorn project.wsgi