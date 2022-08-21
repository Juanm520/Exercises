<?php

$name = $_GET["name"];
$age = $_GET["age"];
 
if ($name = "NULL" || $age= "NULL") {
    echo "No hay datos para la solicitud";
}
else {
    echo "Al parecer eres $name y tienes $age años, puedes acceder a pagar impuestos."; 
}

echo "<pre>";
var_dump($_POST);
echo "</pre>";