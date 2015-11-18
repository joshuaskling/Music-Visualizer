<?php
session_start();
?>
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html" charset="windows-1256" /></head><body>
<form enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
Please choose a file: <input name="file" type="file" /><br />
<input type="submit" value="Upload" /></form>

<?php 

// ----- HELPER FUNCTION AREA 

// METHOD TO EXECUTE ALL KNOWN FLUSH METHODS AND REFILL BUFFER
function hardFlush(){
	ob_end_flush();
	ob_flush();
	flush();
	ob_implicit_flush();
	for ($i=0; $i < 4960; $i++) {
		echo ' ';
	}
}

// METHOD TO RUN A PYTHON SCRIPT
function runPython($cmd){
	$cmd = 'python -u .\pyBlender\Scripts\log.py';
	echo $cmd;
	hardFlush();
	
	// TEST LIVE OUTPUT FROM PHP CORE
	echo "<br>";
	for ($i=0; $i < 5; $i++) {
		echo 'Hi<br>';
		sleep(1);
	}
	
	// TEST LIVE OUTPUT FROM PYTHON SUBPROCESS
	echo "<p>".$cmd."</p>";
	
	$handle = popen($cmd,"r");
	
	while(!feof($handle)) {
		
		$buffer = fread($handle, 1024);
		
		
		echo $buffer."<br/>\n";
		hardFlush();
	}
	pclose($handle);
	
	
	
}


// ----- MAIN FUNCTION EXECUTION AREA
if (!empty($_FILES["file"])){
	if ($_FILES["file"]["error"] > 0){
		echo "Error: " . $_FILES["file"]["error"] . "<br>";
	}
	else{
		echo "Stored file:".$_FILES["file"]["name"]."<br>Size:".($_FILES["file"]["size"]/1024)." kB<br/><br/>";
		//move_uploaded_file($_FILES["file"]["tmp_name"],$_FILES["file"]["name"]);
	}

	// REMOVE ALL KNOWN CACHING MECHANISMS
	ob_start();
	
	ini_set('output_buffering', 'off');
	ini_set('zlib.output_compression', false);
	ini_set('implicit_flush', true);
	ob_implicit_flush(true);
	hardFlush();
	
	// BEGIN SCRIPT EXECUTIONS
	echo('<h1>**PHP Starting pyBlender**</h1>');
	hardFlush();

	runPython();
	
	
	echo('<h1>**pyBlender: Beat Engine**</h1>');
	$com = 'beat_frames.py andre';
	//runPython($com);

	echo('<h1>**pyBlender: Volume Engine**</h1>');
	$com = 'mel_volume.py andre';
	//runPython($com);

	echo('<h1>**pyBlender: Spectrogram Decomposition**</h1>');
	$com = 'n_bin_mel.py andre 8 ';
	//runPython($com);

	echo('<h1>**pyBlender: Core Fusion Engine**</h1>');
	$com = 'core_insert.py VUmeter';
	//runPython($com);

	
	echo('<h1>Done.</h1><br>');

}

else if(0 /*!$_FILES["file"]["name"]*/){
	header('location:test2.php');
}
else {
	// NOTHING
}

?>


</body>
</html>