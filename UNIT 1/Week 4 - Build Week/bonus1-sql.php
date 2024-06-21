<?php
$servername = "localhost";
$username = "root";
$password = "root";
$dbname = "test_db";

// Creare connessione
$conn = new mysqli($servername, $username, $password, $dbname);

// Controllare connessione
if ($conn->connect_error) {
    die("Connessione fallita: " . $conn->connect_error);
}

if (!isset($_GET['id']) || empty($_GET['id'])) {
    $sql = "SELECT * FROM users";

} else {
    $id = $_GET['id'];
    $sql = "SELECT * FROM users WHERE id = $id"; // Per evitare SQL injection: $sql = "SELECT * FROM users WHERE id = ?";
}

    $result = $conn->query($sql);

    if ($result->num_rows > 0) {
        while($row = $result->fetch_assoc()) {
            echo "ID: " . $row["id"]. " - Nome: " . $row["name"]. " - Email: " . $row["email"]. "<br>";
        }
    } else {
        echo "0 risultati";
    }


$conn->close();
?>
