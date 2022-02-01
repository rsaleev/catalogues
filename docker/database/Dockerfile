# syntax=docker/dockerfile:1


ARG PORT=${POSTGRES_PORT}
ARG LANG=${POSTGRES_LANG}


FROM library/postgres:14.1-bullseye

LABEL maintainer="rs.aleev@gmail.com"
# copy initb script
COPY ./docker/database/init-user-db.sh /docker-entrypoint-initdb.d/
# change ownership 
RUN chown postgres:postgres /docker-entrypoint-initdb.d/*.sh
# change mode to executable
RUN chmod +X /docker-entrypoint-initdb.d/*.sh
# copy configuration file
COPY ./docker/database/postgresql.conf /etc/postgresql/


EXPOSE ${PORT}
