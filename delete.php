<?php 
require_once 'includes/initialize.php';
// print_r($_GET);
// echo count($_GET) + 1;
if (count($_GET) == 0 ) {
	echo "No values";
	exit('');
}
$active = $_GET['tab'];
// print_r($_GET);


$newobj =  $active::find_by_id($_GET['id']);
$msg = '';

if ($_GET['json']==1) {
	$toDel = $newobj->filename;
	unlink("uploads".DS.$toDel);
		if (!(file_exists("uploads".DS.$toDel))) {
			$op = "Deleted";
			$del = 1;
			$msg = "&deleted_status=".$del;
		}
	else{
		$op = "Not Deleted";
		$del = 0;
	}
}


$newobj->delete();
			
				redirect_to("others.php?tab={$active}&item={$active}&deleted=true&position={$_GET['next']}".$msg );
					//tab=organization&item=organization




 ?>
 <a href="index.php">Return Home</a>