<?php
plana("No debo hacer harcoding", 20);

function plana($texto, $veces){
	for ($i = 0; $i <= $veces; $i++){
   	echo $texto.", ";
  	}
}
?>