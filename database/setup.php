<?php

function createDatabase() {
    try {
        $conn = new PDO("mysql:host=localhost", "root", "");
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Create database if not exists
        $sql = "CREATE DATABASE IF NOT EXISTS ventas_2025";
        $conn->exec($sql);
        echo "Database created successfully or already exists\n";
        
        // Connect to the new database
        $conn = new PDO("mysql:host=localhost;dbname=ventas_2025", "root", "");
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

        // Create personas table
        $sql = "CREATE TABLE IF NOT EXISTS personas (
            id int(11) NOT NULL AUTO_INCREMENT,
            primer_nombre varchar(50) NOT NULL,
            segundo_nombre varchar(50) DEFAULT NULL,
            primer_apellido varchar(50) NOT NULL,
            segundo_apellido varchar(50) DEFAULT NULL,
            documento varchar(10) NOT NULL,
            telefono varchar(15) NOT NULL,
            correo_electronico varchar(50) NOT NULL,
            direccion_residencia text NOT NULL,
            fecha_nacimiento date NOT NULL,
            genero enum('FEMENINO','MASCULINO') DEFAULT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY documento (documento),
            UNIQUE KEY telefono (telefono),
            UNIQUE KEY correo_electronico (correo_electronico)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci";
        
        $conn->exec($sql);
        echo "Table 'personas' created successfully or already exists\n";

        // Create clientes table
        $sql = "CREATE TABLE IF NOT EXISTS clientes (
            id int(11) NOT NULL AUTO_INCREMENT,
            id_persona int(11) NOT NULL,
            PRIMARY KEY (id),
            UNIQUE KEY id_persona (id_persona),
            CONSTRAINT clientes_ibfk_1 FOREIGN KEY (id_persona) REFERENCES personas (id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci";
        
        $conn->exec($sql);
        echo "Table 'clientes' created successfully or already exists\n";

    } catch(PDOException $e) {
        echo "Error: " . $e->getMessage() . "\n";
    }

    $conn = null;
}

// Execute the database setup
createDatabase();

?>