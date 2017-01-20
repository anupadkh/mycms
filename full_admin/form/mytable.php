<?php 
include_once '../includes/initialize.php'; 
if (isset($_POST['Submit'])) {
	// print_r($_POST);
	$tablename = $_POST['tablename'];
	$header = $_POST['header'];
	$i = 0;
	foreach ($tablename as $table) {
		$my = new mytables();
		$my->tablename = $table;
		$my->header = $header[$i];
		$i++;
		$my->save();
	}
}
?><!DOCTYPE html>
<html>
<head>
	<title>Make your Table Headers</title>
</head>
<body>
<form method="post" action="mytable.php">
<table>
<?php $attributes = get_class_vars("mytables");
function find_by_sql($sql="") {
    global $database;
    $result_set = $database->query($sql);
    $object_array = array();
    while ($row = $database->fetch_array($result_set)) {
      $object_array[] = $row[0];
    }
    return $object_array;
  }

$myarray = find_by_sql('show tables');
// print_r($myarray);
// print_r($myarray);
echo "<tr>";
foreach ($attributes as $one => $key) {
		echo "<th>";
		echo $one . "</th>";
	}
echo "</tr>";
foreach ($myarray as $value) {
	echo "<tr>";
	foreach ($attributes as $one => $key) {
		echo "<td>";
		if ($one == 'id') {
			continue;
		}
		echo "<input type=\"text\" name=\"{$one}[]\" value=\"{$value}\">" . "</td>";
	}
	echo "</tr>";

}
 ?>
 <input type="Submit" name="Submit">
 </table>
 </form>
</body>
</html>