<?php 
include_once '../includes/initialize.php'; 
$all_tables = mytables::find_all();
/* 

- $active stores name of table used
- Use of hidden variable table stores name of table used on submit. Table can't be used in database name as variable . So this name is best
- 


*/
?>

<!DOCTYPE html>
<html>
<head>
<style>
table, th, td {
    border: 1px solid black;
}
</style>
</head>
<body>
<?php
foreach ($all_tables as $table1) {
	echo "<h1>".$table1->tablename."</h1>";

	$sm = ($db->query("desc ".$table1->tablename));
	$i =0;
	echo "<table>";
	
	foreach ($sm as $sm1) {
		// print_r($sm1);
		echo "<tr>";
		if ($i==0) {
			
			foreach ($sm1 as $key => $value) {
				echo "<th>".$key."</th>";
				
			}
			echo "</tr>";
		}
		$i++;
		echo "<tr>";
		foreach ($sm1 as $key => $value) {
			echo "<td>".$value."</td>";

		}
		echo "</tr>";
		// echo "<br/>";	
	}
	echo "</table>";
	
}

?>
</body>
</html>

