<?php
class Connection {
    protected $conn;
    protected $cursor;

    public function __construct() {
        try {
            $host = "localhost";
            $dbname = "ventas_2025";
            $username = "root";
            $password = "";

            $this->conn = new PDO("mysql:host=$host;dbname=$dbname", $username, $password);
            $this->conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
            $this->cursor = $this->conn;
        } catch(PDOException $e) {
            die("Connection failed: " . $e->getMessage());
        }
    }

    public function __destruct() {
        $this->conn = null;
        $this->cursor = null;
    }
}
?>