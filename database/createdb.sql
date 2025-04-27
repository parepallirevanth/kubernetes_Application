CREATE DATABASE dockerdb;
CREATE USER dockeruser WITH PASSWORD '***********';
GRANT ALL PRIVILEGES ON DATABASE "dockerdb" to dockeruser;
