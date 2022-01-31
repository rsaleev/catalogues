# syntax=docker/dockerfile:1


FROM nginx/unit:1.26.1-minimal

ARG RELEASE_VERSION=${RELEASE_VERSION}
ARG OWNER=${OWNER}
ARG REPO=${REPO}
ARG TOKEN=${TOKEN}


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
RUN apt upgrade tar
# install poetry
RUN pip3 install poetry
# create project folder
RUN mkdir -p /var/www/catalogues
# setup working directory
WORKDIR /var/www/catalogues
# copy code and other necessary folder to destination
RUN curl -JLO -H "Authorization: token ${TOKEN}" https://github.com/${OWNER}/${REPO}/archive/${RELEASE_VERSION}.tar.gz
RUN tar -xf ${REPO}-${RELEASE_VERSION}.tar.gz --strip-components=1 
# copy configuration
ADD ./config ./src/
# install python3 requirements
RUN poetry install
# create persistent volume
ADD ./unitd.json /docker-entrypoint.d/config.json
VOLUME ["/var/www", "/var/log/nginx", "/etc/nginx"]
# expose 80 port
EXPOSE 80
# change ownership for isapt-transport-httpsolation
RUN chown -R unit:unit /var/www/catalogues

# STOPSIGNAL SIGTERM

#ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]

CMD ["unitd","--no-daemon","--control","unix:/var/run/control.unit.sock"]
