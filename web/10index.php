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
 <h2>All Programmer</h2>
 <table >
 <tr>
 <th>Id</th>
 <th>Name</th>
 <th>Image</th>
 <th>Action</th>
 </tr>
 <?php 
 $sql = "SELECT * FROM stu_reg";
 $result = $conn -> query($sql);
 while($row = $result -> fetch_assoc()){
 echo "
 <tr>
 <td>$row[id]</td>
 <td>$row[name]</td>
 <td><img src='$row[image]'/></td>
 <td><a class='delete_btn' href='delete.php?id=$row[id]'>Delete</a></td>
 </tr>
 ";
 }
 ?>
 </table>
 </div>
 <a class="add_btn" href="insert.php">Add Prorgammer</a>
 </div>
</body>
</html>