USE reservas_fisi;

-- Las tablas se crean automáticamente, pero puedes agregar datos iniciales:
INSERT IGNORE INTO usuarios (correo, password_hash, rol) VALUES
('adminfisi@unmsm.edu.pe', 'FISI2024', 'admin');

-- Insertar usuarios de prueba para desarrollo
INSERT IGNORE INTO usuarios (correo, password_hash, rol) VALUES
('alumno1@unmsm.edu.pe', 'EXTERNA', 'student'),
('alumno2@unmsm.edu.pe', 'EXTERNA', 'student'),
('docente1@unmsm.edu.pe', 'EXTERNA', 'student');

SELECT 'Base de datos reservas_fisi configurada correctamente' AS Estado;