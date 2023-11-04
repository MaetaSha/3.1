<?php
$servername = "localhost";
$username = "root";
$password = "";

// Create a connection to MySQL
$conn = new mysqli($servername, $username, $password);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Create a database called "Programmer" if it doesn't exist
$sql = "CREATE DATABASE IF NOT EXISTS Programmer";

if ($conn->query($sql) === TRUE) {
    echo "Database created successfully<br>";
} else {
    echo "Error creating database: " . $conn->error;
}

// Select the "Programmer" database
$conn->select_db("Programmer");

// SQL statement to create the "Stu_Reg" table
$sql = "CREATE TABLE IF NOT EXISTS Stu_Reg (
    ID VARCHAR(30) PRIMARY KEY,
    Name TEXT,
    Image VARCHAR(400),
    Password VARCHAR(20) NOT NULL
)";

if ($conn->query($sql) === TRUE) {
    echo "Table created successfully";
} else {
    echo "Error creating table: " . $conn->error;
}

// Close the MySQL connection
$conn->close();
?>