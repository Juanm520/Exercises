<?php 
$tabla_del_9 = [];

for ($i=1; $i <= 50; $i++) {
    $productos = 9 * $i;
    $factores_producto = "9 x $i = $productos";
    array_push($tabla_del_9, $factores_producto);
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tabla del 9</title>
</head>
<body>
   <h1>Tabla del 9 - Factor 50</h1> 
    <ul>
        <?php foreach($tabla_del_9 as $factor_producto):?>
            <li> <?= $factor_producto?></li> 
        <?php endforeach; ?>
    </ul>
</body>
</html>