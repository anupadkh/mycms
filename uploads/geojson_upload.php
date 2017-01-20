<?php
require_once '../includes/initialize.php';
ini_set('upload_max_filesize', '20M');
$target_dir = "geojsons/";
print_r($_FILES);
$target_file = $target_dir . time(). basename($_FILES["filename"]["name"]);
$uploadOk = 1;
$imageFileType = pathinfo($target_file,PATHINFO_EXTENSION);
$imageFileType = strtolower($imageFileType);
echo "Filetype =". $imageFileType."<br/>";
// Check if image file is a actual image or fake image
if(isset($_POST["submit"])) {
    /*$check = getimagesize($_FILES["fileToUpload"]["tmp_name"]);
    if($check !== false) {
        echo "File is an image - " . $check["mime"] . ".";
        $uploadOk = 1;
    } else {
        echo "File is not an image.";
        $uploadOk = 0;
    }*/

    // Check if file already exists
    if (file_exists($target_file)) {
        echo "Sorry, file already exists.";
        $uploadOk = 0;
    }
    // Check file size
    
    // Allow certain file formats
    if($imageFileType != "json" ) {
        echo "Sorry, only JSON";
        $uploadOk = 0;
    }
    // Check if $uploadOk is set to 0 by an error
    if ($uploadOk == 0) {
        echo "Sorry, your file was not uploaded.";
    // if everything is ok, try to upload file
    } else {
        if (move_uploaded_file($_FILES["filename"]["tmp_name"], $target_file)) {
            echo "The file ". basename( $_FILES["filename"]["name"]). " has been uploaded.";
            $file = new attr_geojsonfile();
            $file->id = $_POST['id'];
            $file->filename = $target_file;
            $file->cs = $_POST['cs'];
            $file->correc = $_POST['correc'];
            $file->layername = $_POST['layername'];
            $file->identifiername = $_POST["identifiername"];
            $file->save();
            echo "Saved";
            redirect_to("../geojson.php?tab=".$_POST['nav_table']."&id=".$file->id."&position=".$_POST['position']);
        } else {
            echo "Sorry, there was an error uploading your file.";
        }
    }
}
?>
