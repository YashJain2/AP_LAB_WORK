<?php
if(isset($_POST["form_submitted"]))
{
		if(!isset($_POST["agree"]))
		echo "You haven't agreed to the terms and services";
		else
		echo "Thank You !<br>".$_POST["firstname"]." ".$_POST["firstname"]." you have been successfully registered";
}
 ?>
