<?php 
//form.php
require_once '../includes/initialize.php';
if (isset($_GET['table'])) {
	$table = $_GET['table'];
	// echo "SELECT * FROM fields WHERE tablename={$table}";
	print_r($fields::find_by_sql("SELECT * FROM fields WHERE 'tablename'='{$table}'"));
}
 ?>