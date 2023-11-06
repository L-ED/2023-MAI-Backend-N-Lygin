FROM ubuntu:20.04
ADD . /app
RUN apt-get update
ENV TZ=Europe/Amsterdam
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get install -y python3.8 python3-dev python3-pip postgresql postgresql-contrib nginx build-essential libpq-dev
RUN pip3 install -r /app/requirements.txt
RUN cp /app/nginx.conf /etc/nginx/nginx.conf
# RUN 
USER nobody
WORKDIR /app
CMD /bin/bash entrypoint.sh