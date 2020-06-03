FROM postgres
ADD . /tmp/chatapp
WORKDIR /tmp/chatapp
COPY createdb.sql /docker-entrypoint-initdb.d
