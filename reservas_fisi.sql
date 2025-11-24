-- Crear base de datos si no existe
CREATE DATABASE IF NOT EXISTS reservas_fisi;

USE reservas_fisi;

-- Insertar datos iniciales
INSERT IGNORE INTO usuarios (correo, password_hash, rol) VALUES
('adminfisi@unmsm.edu.pe', 'FISI2024', 'admin'),
('alumno1@unmsm.edu.pe', 'EXTERNA', 'student'),
('alumno2@unmsm.edu.pe', 'EXTERNA', 'student'),
('docente1@unmsm.edu.pe', 'EXTERNA', 'student');

SELECT 'Base de datos reservas_fisi configurada correctamente' AS Estado;