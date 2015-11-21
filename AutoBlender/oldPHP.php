<?php
session_start();
?>
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html" charset="windows-1256" /></head>
<body>
<form enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
Please choose a file (it doesn't do anything, don't worry): 
<input name="file" type="file" /><br />
<input type="submit" value="Begin Server Test" />
</form><br>

<?php 

// ----- HELPER FUNCTION AREA 

//METHOD TO KEEP HTML CLEAN
function printh($subject){
	echo "\n".$subject."<br>";
}

// METHOD TO EXECUTE ALL KNOWN FLUSH METHODS AND REFILL BUFFER
function hardFlush(){
	ob_end_flush();
	ob_flush();
	flush();
	ob_implicit_flush();
	for ($i=0; $i < 4150; $i++) {
		echo ' ';
	}
}

// METHOD TO RUN A PYTHON SCRIPT
function runPython($cmd){
	printh("System Call:");
	$cmd = "python -u .\pyBlender\Scripts\\".$cmd;
	printh($cmd);
	hardFlush();
	
	//* TEST LIVE OUTPUT FROM PHP CORE
	printh("");
	printh("PHP - Live Output Test:");
	printh("------------------------------");
	$testLength = 5;
	for ($i=0; $i < $testLength; $i++) {
		printh("Waiting ".($testLength-$i).'...');
		sleep(1);
		}
	//*/
	
	//* TEST LIVE OUTPUT FROM PYTHON SUBPROCESS
	printh("<br>**Starting System Call**<br>");
	system($cmd." 2>consoleERR.txt&");
	//*/
}


// ----- MAIN FUNCTION EXECUTION AREA
if (!empty($_FILES["file"])){
	if ($_FILES["file"]["error"] > 0){
		echo "Error: " . $_FILES["file"]["error"] . "<br>";
	}
	else{
		echo "Selected file: ".$_FILES["file"]["name"]."<br>Size: ".(int)($_FILES["file"]["size"]/1024)." kB<br/><br/>";
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
	$testFlag = true;
	$forceRun = false;
	
	// LIVE SCRIPT TESTING AREA
	if ($testFlag){
		printh('<h1>**PHP - Starting System Test**</h1>');
		printh('<h1>**Running Python Test Script**</h1>');
		$com = 'pyTest.py'.' arg[1]'.' arg[2]'.' etc...';
		sleep(.1);
		runPython($com);
	}
	// pyBlender FUNCTION AREA
	else if (!$testFlag || $forceRun) {
		printh('<h1>**PHP Starting pyBlender**</h1>');
		
		//* RUN LIBROSA BEAT ANALYZER
		printh('<h1>**pyBlender: Beat Engine**</h1>');
		$com = 'beat_frames.py andre';
		runPython($com);
		//*/
		
		//* RUN LIBROSA VOLUME ANALYZER
		printh('<h1>**pyBlender: Volume Engine**</h1>');
		$com = 'mel_volume.py andre';
		runPython($com);
		//*/
		
		//* RUN LIBROSA MEL SPECTROGRAM ANALYZER
		printh('<h1>**pyBlender: Spectrogram Decomposition**</h1>');
		$com = 'n_bin_mel.py andre 8';
		runPython($com);
		//*/
		
		//* FUSE CORE AND RENDERING SCRIPT
		printh('<h1>**pyBlender: Core Fusion Engine**</h1>');
		$com = 'core_insert.py VUmeter';
		runPython($com);
		//*/
	}
	
	printh('<h1>**PHP Scripts Done**</h1><br>');
	
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