<?php 
 require_once("connection.php");
 $targetDir = "images/";
 if(isset($_POST['id']) && isset($_POST['name'])&& isset($_FILES['image']) && 
isset($_POST['password'])){
 $id = $_POST['id'];
 $name = $_POST['name'];
 $password = (string)md5($_POST['password']);
 $fileName = basename($_FILES['image']['name']);
 $targetFilePath = $targetDir.$fileName;
 $image = (string)$targetFilePath;
 
 $sql = "INSERT INTO stu_reg(id, name, image, p_password)
 VALUES('$id', '$name', '$image', '$password')";
 
 $result = $conn -> query($sql);
 if($result){
 move_uploaded_file($_FILES['image']['tmp_name'], $targetFilePath);
 header("location: index.php");
 }
 else{
 echo "Not Added";
 }
 
 }
?>
<!DOCTYPE html>
<html lang="en">
<head>
 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>Add Student</title>
 <link rel="stylesheet" href="style.css">
</head>
<body>
 <div class="container">
 <div class="form">
 <h2>Add Programmer</h2>
 <form method="POST" enctype="multipart/form-data">
<table>
 <tr>
 <td><label for="id">Id</label></td>
 <td><input type="text" id="id" name="id"></td>
 </tr>
 <tr>
 <td><label for="name">Name</label></td>
 <td><input type="text" id="name" name="name"></td>
 </tr>
 <tr>
 <td><label for="image">Upload Profile</label></td>
 <td><input type="file" id="image" name="image"></td>
 </tr>
 <tr>
 <td><label for="password">Password</label></td>
 <td><input type="password" id="password" name="password"></td>
 </tr>
 <tr>
 <td></td>
 <td><input type="submit" name="submit" value="submit"></td>
 </tr>
 </table>
 </form>
 </div>
 </div>
</body>
</html>