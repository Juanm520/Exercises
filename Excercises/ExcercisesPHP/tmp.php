<?php
// Crear un fichero en el temporal 
// directorio de archivos utilizando sys_get_temp_dir()
$temp_file = tempnam(sys_get_temp_dir(), 'Tux');

echo $temp_file;
?>