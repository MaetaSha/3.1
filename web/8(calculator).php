<?php
$sum = null;
$opa = null;
$x = 0;
$y = 0;

if (isset($_POST["ADD"])) {
    $x = $_POST['fnum'];
    $y = $_POST['snum'];
    $opa = '+';
    $sum = $x + $y;
} else if (isset($_POST["SUB"])) {
    $x = $_POST['fnum'];
    $y = $_POST['snum'];
    $opa = '-';
    $sum = $x - $y;
} else if (isset($_POST["MUL"])) {
    $x = $_POST['fnum'];
    $y = $_POST['snum'];
    $opa = '*';
    $sum = $x * $y;
} else if (isset($_POST["DIV"])) {
    $x = $_POST['fnum'];
    $y = $_POST['snum'];
    $opa = '/';
    $sum = number_format($x / $y, 3);
}
?>

<html>
<head>
    <style>
        body {
            background-color: #f0f0f0;
            font-size: 30px;
        }

        .div2 {
            height: 80%;
            width: 45%;
            float: left;
            font-size: 30px;
            margin: auto;
            border-radius: 8px;
            border-color: gold;
        }

        .div1 {
            height: 80%;
            width: 50%;
            float: right;
            border-radius: 8px;
            border-color: gold;
        }

        .cal {
            height: 20%;
            font-size: 50px;
            color: blue;
            margin: auto;
            border-radius: 8px;
            border-color: gold;
        }

        input {
            font-size: 30px;
            font-family: 'Times New Roman';
        }

        textarea {
            font-size: 30px;
            border-radius: 8px;
        }

        label {
            color: red;
        }

        .vl {
            border-right: 2px solid black;
            height: 250px;
        }
    </style>
</head>
<body>
    <div class="cal">A simple Calculator</div>
    <hr/>
    <div class="div1">
        <label>Result</label>
        <hr/>
        <textarea rows="3" cols="33">
            <?php
            if ($sum == null) {
                echo "$sum";
            } else {
                echo " $x $opa $y = $sum";
            }
            ?>
        </textarea>
    </div>
    <div class="div2">
        <div class="vl">
            <form method="post" action="eightS.php">
                <label>Input</label>
                <hr/>
                Enter 1st number <input type="text" name="fnum" required/><br/><br/>
                Enter 2nd number <input type="text" name="snum" required/><hr/>
                <input type="submit" name="ADD" value="ADD"/>
                <input type="submit" name="SUB" value="SUB"/>
                <input type="submit" name="MUL" value="MUL"/>
                <input type="submit" name="DIV" value="DIV"/>
            </form>
        </div>
    </div>
</body>
</html>
