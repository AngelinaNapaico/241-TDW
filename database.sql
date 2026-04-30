CREATE DATABASE IF NOT EXISTS contactanos_db;
USE contactanos_db;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    message TEXT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);