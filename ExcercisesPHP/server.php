<?php

$name = $_GET["name"];
$age = $_GET["age"];
$namePost = $_POST["namePost"];
$agePost = $_POST["agePost"];

if ($name == "" || $age== "") {
    echo "No hay datos para la solicitud GET. <br>";
    
}
else {
    echo "Al parecer eres $name y tienes $age años, puedes acceder a pagar impuestos. <br>"; 
}

if ($namePost == "" || $agePost== "") {
    echo "No hay datos para la solicitud POST";
}
else {
    echo "Al parecer eres $namePost y tienes $agePost años, puedes acceder a pagar impuestos."; 
}
