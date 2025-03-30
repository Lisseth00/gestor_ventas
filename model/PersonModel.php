<?php
require_once 'Connection.php';

class PersonModel extends Connection {
    public function __construct() {
        parent::__construct();
    }

    public function agregarPersona($datos) {
        try {
            $sql = "INSERT INTO personas (
                primer_nombre, 
                segundo_nombre, 
                primer_apellido, 
                segundo_apellido,
                documento, 
                telefono, 
                correo_electronico, 
                direccion_residencia,
                fecha_nacimiento, 
                genero
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)";

            $stmt = $this->conn->prepare($sql);
            $stmt->execute([
                $datos['primer_nombre'],
                $datos['segundo_nombre'],
                $datos['primer_apellido'],
                $datos['segundo_apellido'],
                $datos['documento'],
                $datos['telefono'],
                $datos['correo_electronico'],
                $datos['direccion_residencia'],
                $datos['fecha_nacimiento'],
                $datos['genero']
            ]);
            return true;
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return false;
        }
    }

    public function obtenerPersonas() {
        try {
            $stmt = $this->conn->query("SELECT * FROM personas");
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return [];
        }
    }

    public function obtenerPersonaPorId($id) {
        try {
            $stmt = $this->conn->prepare("SELECT * FROM personas WHERE id = ?");
            $stmt->execute([$id]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return null;
        }
    }

    public function actualizarPersona($id, $datos) {
        try {
            $sql = "UPDATE personas SET 
                primer_nombre = ?,
                segundo_nombre = ?,
                primer_apellido = ?,
                segundo_apellido = ?,
                documento = ?,
                telefono = ?,
                correo_electronico = ?,
                direccion_residencia = ?,
                fecha_nacimiento = ?,
                genero = ?
                WHERE id = ?";

            $stmt = $this->conn->prepare($sql);
            $stmt->execute([
                $datos['primer_nombre'],
                $datos['segundo_nombre'],
                $datos['primer_apellido'],
                $datos['segundo_apellido'],
                $datos['documento'],
                $datos['telefono'],
                $datos['correo_electronico'],
                $datos['direccion_residencia'],
                $datos['fecha_nacimiento'],
                $datos['genero'],
                $id
            ]);
            return true;
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return false;
        }
    }

    public function eliminarPersona($id) {
        try {
            $stmt = $this->conn->prepare("DELETE FROM personas WHERE id = ?");
            $stmt->execute([$id]);
            return true;
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return false;
        }
    }
}
?>
