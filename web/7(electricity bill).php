
 
 <?php
$unit = ""; // Initialize the $unit variable
$p = "";

if (isset($_POST["unit"])) {
    $unit = $_POST["unit"];
    $price = 0;

    if ($unit <= 50) {
        $price = $unit * 3.5;
    } elseif ($unit > 50 && $unit <= 100) {
        $price = $unit * 4.0;
    } elseif ($unit > 100 && $unit <= 200) {
        $price = $unit * 5.20;
    } else {
        $price = $unit * 6.50;
    }

    $p = "<p> Unit is: " . $unit . " Bill is " . $price . " Taka</p>";
}
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Electric Bill</title>
    <style>
        body {
            margin: 0;
        }

        .form_style {
            width: 300px;
            margin: auto;
        }

        form {
            margin-top: 80px;
            font-family: arial;
        }

        form label {
            margin-bottom: 10px;
            display: block;
            font-size: 18px;
        }

        form button {
            margin-top: 10px;
            padding: 3px 10px;
            border: 1px solid #000;
            background: #000;
            color: #fff;
            font-size: 18px;
            border-radius: 2px;
        }
    </style>
</head>
<body>
    <div class="form_style">
        <form action="" method="post">
            <label for="unit">Enter your number of units</label>
            <input type="number" id="unit" name="unit" value="<?php echo $unit ?>">
            <br>
            <button type="submit">Submit</button>
        </form>
        <?php echo $p; ?>
    </div>
</body>
</html>
