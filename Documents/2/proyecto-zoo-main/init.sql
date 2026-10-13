USE zoologico;

CREATE TABLE animales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    especie VARCHAR(100),
    color VARCHAR(50)
);

INSERT INTO animales (nombre, especie, color)
VALUES
('Simba', 'León', 'cafe'),
('Manny', 'Elefante', 'gris'),
('Roco', 'Tigre', 'naranja'),
('Lola', 'Jirafa', 'amarilla');