<?php
 require_once("connection.php");
 $id = "";
 $name = "";
 $session = "";
 $phone = "";
 $city = "";
 $gender = "";
 $error_message = "";
 $success_message = "";
 if($_SERVER['REQUEST_METHOD'] == 'GET'){
 if(!isset($_GET["id"])){
 header("location: index.php");
 exit;
 
}
 $id = $_GET["id"];
 $sql = "SELECT * FROM semester_reg WHERE id=$id";
 $result = $conn 
-> query($sql);
 $row = $result 
-> fetch_assoc();
 if(!$row){
 header("location: index.php");
 exit;
 
}
 $id = $row["id"];
 $name = $row["name"];
 $session = $row["st_session"];
 $phone = $row["phone"];
 $city = $row["city"];
 $gender = $row["gender"];
 
}
 else{
 $id = $_POST["id"];
 $name = $_POST["name"];
 $session = $_POST["session"];
 $phone = $_POST["phone"];
 $city = $_POST["city"];
 $gender = $_POST["gender"];
do{
 if(empty($name) || empty($session) || empty($phone) || empty($city) || empty($gender)){
 $error_message = "All fields are required";
 break;
 }
 // add new data
 $sql = "UPDATE semester_reg 
 SET name='$name', 
 st_session='$session', 
 phone='$phone', 
 city='$city', 
 gender='$gender'
 WHERE id=$id ";
 $result = $conn -> query($sql);
 if(!$result){
 $error_message = "Invalid query". $conn -> error;
 break;
 }
 
 header("location: index.php");
 exit;
 } while(true);
 }
 $conn->close();
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
 <h2>Add Student</h2>
 <?php if(!empty($error_message)) echo "<p class='error_message'>$error_message</p>"; ?>
 <form method="POST">
 <input type="hidden" name="id" value="<?php echo $id; ?>">
 <table>
<tr>
 <td><label for="name">Student Name</label></td>
 <td><input type="text" id="name" name="name" value="<?php echo $name; ?>"></td>
 </tr>
 <tr>
 <td><label for="session">Session</label></td>
 <td><input type="text" id="session" name="session" value="<?php echo $session; ?>"></td>
 </tr>
 <tr>
 <td><label for="phone">Phone</label></td>
 <td><input type="text" id="phone" name="phone" value="<?php echo $phone; ?>"></td>
 </tr>
 <tr>
 <td><label for="city">City</label></td>
 <td><input type="text" id="city" name="city" value="<?php echo $city; ?>"></td>
 </tr>
 <tr>
 <td>Gender</td>
 <td>
 <input type="radio" id="male" name="gender" value="Male"> <span>Male</span>
 <input type="radio" id="female" name="gender" value="Female"> <span>Female</span>
 </td>
 </tr>
 <tr>
 <td></td>
 <td><input type="submit" value="Update"></td>
 </tr>
 </table>
 <?php if(!empty($success_message)) echo "<p class='success_message'>$success_message</p>"; 
?>
 </form>
 </div>
 </div>
</body>
</html>