<?php
$host = "localhost";
$username = "root";
$password = "";
$database = "Programmer";

// Create a connection to the database
$connect = mysqli_connect($host, $username, $password, $database);

if (!$connect) {
    die("Connection failed: " . mysqli_connect_error());
}

// Task 1: Create the "Stu_Reg" table
$createTableSQL = "CREATE TABLE IF NOT EXISTS Stu_Reg (
    ID VARCHAR(30) PRIMARY KEY NOT NULL,
    Name TEXT,
    Image VARCHAR(400),
    Password VARCHAR(20) NOT NULL
)";
$result = mysqli_query($connect, $createTableSQL);

if ($result) {
    echo "Task 1: 'Stu_Reg' table created successfully.<br>";
} else {
    echo "Error creating table: " . mysqli_error($connect);
}

// Task 3: Insert sample data with password encryption and image upload
if (isset($_POST["insert"])) {
    $id = $_POST["id"];
    $name = $_POST["name"];
    $password = password_hash($_POST["password"], PASSWORD_BCRYPT);

    // Handle file upload
    $image = "";
    if ($_FILES["image"]["name"]) {
        $imageDir = "uploads/";
        if (!is_dir($imageDir)) {
            mkdir($imageDir);
        }
        $imagePath = $imageDir . $_FILES["image"]["name"];
        if (move_uploaded_file($_FILES["image"]["tmp_name"], $imagePath)) {
            $image = $imagePath;
        }
    }

    $insertSQL = "INSERT INTO Stu_Reg (ID, Name, Image, Password) VALUES ('$id', '$name', '$image', '$password')";
    $result = mysqli_query($connect, $insertSQL);

    if ($result) {
        echo "Task 3: Data inserted successfully.<br>";
    } else {
        echo "Error inserting data: " . mysqli_error($connect);
    }
}

// Task 4: Show all records based on ID and name
if (isset($_POST["view"])) {
    $id = $_POST["id"];
    $name = $_POST["name"];

    $selectSQL = "SELECT * FROM Stu_Reg WHERE ID='$id' AND Name='$name'";
    $result = mysqli_query($connect, $selectSQL);

    if ($result) {
        echo "Task 4: View Records:<br>";
        echo "<table border='1'><tr><th>ID</th><th>Name</th><th>Image</th><th>Password</th></tr>";

        while ($row = mysqli_fetch_assoc($result)) {
            echo "<tr><td>" . $row['ID'] . "</td><td>" . $row['Name'] . "</td><td>" . $row['Image'] . "</td><td>" . $row['Password'] . "</td></tr>";
        }

        echo "</table>";
    } else {
        echo "Task 4: No record found!<br>";
    }
}

// Task 5: Delete a single record based on ID and name
if (isset($_POST["delete"])) {
    $id = $_POST["id"];
    $name = $_POST["name"];

    $deleteSQL = "DELETE FROM Stu_Reg WHERE ID='$id' AND Name='$name'";
    $result = mysqli_query($connect, $deleteSQL);

    if ($result) {
        echo "Task 5: Record deleted successfully.<br>";
    } else {
        echo "Task 5: Error deleting record: " . mysqli_error($connect);
    }
}

mysqli_close($connect);
?>

<!DOCTYPE html>
<html>
<head>
    <title>Student Registration Form</title>
</head>
<body>
    <h2>Student Registration Form</h2>
    <form method="post" action="programmer.php" enctype="multipart/form-data">
        <table border="1">
            <tr>
                <th>ID</th>
                <td><input type="text" name="id" required></td>
            </tr>
            <tr>
                <th>Name</th>
                <td><input type="text" name="name"></td>
            </tr>
            <tr>
                <th>Image</th>
                <td><input type="file" name="image"></td>
            </tr>
            <tr>
                <th>Password</th>
                <td><input type="password" name="password" required></td>
            </tr>
            <tr>
                <td colspan="2">
                    <input type="submit" name="insert" value="Insert Data">
                    <input type="submit" name="view" value="View Data">
                    <input type="submit" name="delete" value="Delete Data">
                </td>
            </tr>
        </table>
    </form>
</body>
</html>
  