<?php 
 require_once("connection.php");
?>
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Student info</title>
 <link rel="stylesheet" href="style.css">
</head>
<body>
 <div class="container">
 <div class="table">
 <h2>All Students</h2>
 <table >
 <tr>
 <th>Id</th>
 <th>Name</th>
 <th>Session</th>
 <th>Phone number</th>
 <th>City</th>
 <th>Gender</th>
 <th>Action</th>
 </tr>
 <?php 
 $sql = "SELECT * FROM semester_reg";
 $result = $conn -> query($sql);
 while($row = $result -> fetch_assoc()){
 echo "<tr>
 <td>$row[id]</td>
 <td>$row[name]</td>
 <td>$row[st_session]</td>
 <td>$row[phone]</td>
 <td>$row[city]</td>
 <td>$row[gender]</td>
 <td>
 <a class='edit_btn' href='edit.php?id=$row[id]'>Edit</a>
 <a class='delete_btn' href='delete.php?id=$row[id]'>Delete</a>
 </td>
 </tr>";
}
 $conn->close();
 ?>
 </table>
 </div>
 <a class="add_btn" href="insert.php">Add Student</a>
 </div>
</body>
</html>