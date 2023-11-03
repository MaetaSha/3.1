<?php

$result_str=$result="";
if(isset($_POST["submit"])){
    $units=$_POST['units'];
    if(!empty($units)){
        $result=calculate_bill($units);
        $result_str='Total amount of '. $units.' units = '.$result.' Taka';
        // echo $result_str;
    }
}
function calculate_bill($units){
    $first_unit_cost=3.50;
    $second_unit_cost=4.00;
    $third_unit_cost=5.20;
    $fourth_unit_cost=6.50;

    if($units<=50){
        $bill=$units*$first_unit_cost;
        // echo $bill;
        return $bill;
    }
    else if ($units>50 && $units<=100){
        $temp=50*$first_unit_cost;
        $remain_units=$units-50;
        $bill=$temp+($remain_units*$second_unit_cost);
        return $bill;

    }
    else if ($units>100 && $units<= 200){
        $temp= (50*3.5)+(100*$second_unit_cost);
        $remain_units=$units-150;
        $bill=$temp+($remain_units*$third_unit_cost);
        return $bill;
    }
    else{
        $temp=(50*3.5)+(100*$second_unit_cost)+(100*$third_unit_cost);
        $remain_units=$units-250;
        $bill=$temp+($remain_units*$fourth_unit_cost);
        return $bill;
    }
    // return number_format((float)$bill,2,'.','');
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Electricity Bill</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container">
    <h1>Calculate Electricity Bill</h1>
        <form class="form" action="" method="POST">
        <label for="unit">Units:</label>
        <input type="text" name="units" id="unit" placeholder="Please enter no. of Units">
        <button name="submit">Submit</button><br>
        <?php echo $result_str ?>
        </form>
    </div>
    
</body>
</html>
