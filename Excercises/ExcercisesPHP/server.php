<?php

// $name = $_GET["name"];
// $age = $_GET["age"];
// $name_post = $_POST["name_post"];
// $age_post = $_POST["age_post"];

// $file_name = $_FILES["file"]["name"];

// $path = "files/$file_name";

// if ($name == "" || $age== "") {
//     echo "No hay datos para la solicitud GET. <br>";
    
// }
// else {
//     echo "Al parecer eres $name y tienes $age años, puedes acceder a pagar impuestos. <br>"; 
// }

// if ($name_post == "" || $age_post== "") {
//     echo "No hay datos para la solicitud POST. <br>";
// }
// else {
//     echo "Al parecer eres $name_post y tienes $age_post años, puedes acceder a pagar impuestos. <br>"; 
// }

// echo "<pre>";
// var_dump($file_name);
// echo "</pre>";

echo "<pre>";
var_dump($_FILES);
echo "</pre>";

// echo "<pre>";
// var_dump($path);
// echo "</pre>";


// move_uploaded_file($file, $path);

// echo "$file_name has been upload";