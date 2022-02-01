# syntax=docker/dockerfile:1

FROM nginx/unit:1.26.1-minimal

LABEL maintainer="rs.aleev@gmail.com"
# install python 3
RUN apt update && apt install -y python3.9 python3-pip 
# download and install nginx-unit
RUN apt update && apt install -y curl apt-transport-https gnupg2 lsb-release  \
debian-archive-keyring                                                         \
&&  curl -o /usr/share/keyrings/nginx-keyring.gpg                              \     
https://unit.nginx.org/keys/nginx-keyring.gpg                                  \
    && echo "deb [signed-by=/usr/share/keyrings/nginx-keyring.gpg]            \
           https://packages.nginx.org/unit/debian/ `lsb_release -cs` unit"    \
           > /etc/apt/sources.list.d/unit.list
RUN apt update && apt install -y unit-python3.9                               
RUN apt autoremove --purge --allow-remove-essential -y
RUN apt remove -y lsb-release               \                                                       
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list
# create project folder
RUN mkdir -p /var/www/catalogues
# setup working directory
WORKDIR /var/www/catalogues
# copy configuration
ADD ./docker/app/requirements.txt .
# install python3 requirements
RUN pip3 install -r requirements.txt
COPY src ./src
# create persistent volume
COPY ./app/docker/config.json /docker-entrypoint.d/config.json
# expose 80 port
EXPOSE 80
# change ownership for isapt-transport-httpsolation
RUN chown -R unit:unit /var/www/catalogues


CMD ["unitd","--no-daemon","--control","unix:/var/run/control.unit.sock"]
