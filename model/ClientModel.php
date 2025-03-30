<?php
require_once 'Connection.php';

class ClientModel extends Connection {
    public function __construct() {
        parent::__construct();
    }

    public function agregarCliente($idPersona) {
        try {
            $stmt = $this->conn->prepare("INSERT INTO clientes (id_persona) VALUES (?)");
            $stmt->execute([$idPersona]);
            return true;
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return false;
        }
    }

    public function obtenerClientes() {
        try {
            $sql = "SELECT c.id, p.* FROM clientes c 
                    JOIN personas p ON c.id_persona = p.id";
            $stmt = $this->conn->query($sql);
            return $stmt->fetchAll(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return [];
        }
    }

    public function obtenerClientePorId($id) {
        try {
            $sql = "SELECT c.id, p.* FROM clientes c 
                    JOIN personas p ON c.id_persona = p.id 
                    WHERE c.id = ?";
            $stmt = $this->conn->prepare($sql);
            $stmt->execute([$id]);
            return $stmt->fetch(PDO::FETCH_ASSOC);
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return null;
        }
    }

    public function eliminarCliente($id) {
        try {
            $stmt = $this->conn->prepare("DELETE FROM clientes WHERE id = ?");
            $stmt->execute([$id]);
            return true;
        } catch(PDOException $e) {
            echo "Error: " . $e->getMessage();
            return false;
        }
    }
}
?>