-- create BU courses database
CREATE DATABASE IF NOT EXISTS courses_db;
USE courses_db;

CREATE TABLE IF NOT EXISTS courses_db (
    name VARCHAR(255),
    code VARCHAR(100) PRIMARY KEY,
    description TEXT,
    credit FLOAT,
    prereq TEXT,
    hub TEXT
);