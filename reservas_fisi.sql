-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS reservas_fisi;

USE reservas_fisi;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    correo VARCHAR(255),
    password_hash VARCHAR(255),
    rol VARCHAR(50)
);

CREATE TABLE reservas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    fecha DATE,
    hora_inicio VARCHAR(20),
    hora_fin VARCHAR(20),
    estado VARCHAR(50),

    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

CREATE TABLE bloqueos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE,
    hora_inicio VARCHAR(20),
    hora_fin VARCHAR(20),
    tipo VARCHAR(50)
);

-- Insertar datos iniciales
INSERT IGNORE INTO usuarios (correo, password_hash, rol) VALUES
('adminfisi@unmsm.edu.pe', 'FISI2024', 'admin'),
('alumno1@unmsm.edu.pe', 'EXTERNA', 'student'),
('alumno2@unmsm.edu.pe', 'EXTERNA', 'student'),
('docente1@unmsm.edu.pe', 'EXTERNA', 'student');

SELECT 'Base de datos reservas_fisi configurada correctamente' AS Estado;