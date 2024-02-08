FROM ubuntu:latest

# update the package list
RUN apt update

# install ping and wget
RUN apt install -y iputils-ping wget

# install the mongosh package
RUN wget -qO- https://www.mongodb.org/static/pgp/server-7.0.asc | tee /etc/apt/trusted.gpg.d/server-7.0.asc

# add the MongoDB repository
RUN echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu jammy/mongodb-org/7.0 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-7.0.list

# update packages
RUN apt update

# install the MongoDB package
RUN apt install -y mongodb-mongosh

# copy certificates for TLS auth
COPY db/certs/* /etc/ssl/

