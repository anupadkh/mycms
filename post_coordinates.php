<!DOCTYPE html>
<html>
<head>
	<title>Bridge Database</title>
</head>
<body>
<script src="https://code.jquery.com/jquery-3.1.0.min.js"></script>
<script type="text/javascript">
function loadRows(tag,lat='',long='') {
	// Find a <table> element with id="myTable":
	var table = document.getElementById("myTable");

	// Create an empty <tr> element and add it to the 1st position of the table:
	var row = table.insertRow(0);

	// Insert new cells (<td> elements) at the 1st and 2nd position of the "new" <tr> element:
	var cell1 = row.insertCell(0);
	var cell2 = row.insertCell(1);

	if (tag.placeholder) {
		var leng = tag.value.match(/\n/g).length;
		// var text = tag.value.;	
		var text = leng;
		tag.value = "";
	} else{
		var text = "";
	}
	

	// Add some text to the new cells:
	cell1.innerHTML = "<input type='text' name='latitude[]' placeholder='latitude' value='" + lat + "'>";
	cell2.innerHTML = "<input type='text' name='longitude[]' placeholder='longitude' value='" + long + "'>";	
}

</script>
<form action="index.php" method="post">

	<table id="myTable"></table>
	<textarea rows="4" cols="50" placeholder="Paste from Excel" id="mytextarea"></textarea>
	<button onclick="loadRows('ram');" type="reset">Add new</button>

	<div id ="result"></div>
	<input type="submit" name="submit">
</form>
<script type="text/javascript">
$('#mytextarea').bind('paste', function(e){
    window.setTimeout(function(){
        var text = '';
        var count = 0;
        $($('#mytextarea').val().split('\n')).each(function(i,v){
            console.log(v);
            if (v != "") {
            	var lat = v.split('\t')[0];
	            var long = v.split('\t')[1];
	            loadRows(count, lat, long);	
            }
            
            v = $.trim(v);
            if (v.length > 0) {
            	text+= v+'\n';
            	count++;
            	// console.log(count);
            }
            
        });
        // console.log(text);
        $('#result').html(count);


        // loadRows($('#mytextarea'));
    },1);
});
</script>
<?php 
print_r($_POST) ?>
</body>
</html>