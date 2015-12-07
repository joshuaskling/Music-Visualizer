
<!DOCTYPE html><html><head>

<meta http-equiv="Content-Type" content="text/html" charset="windows-1256" /></head>

<form enctype="multipart/form-data" action='<?php echo $_SERVER["PHP_SELF"]; ?>' method="POST">
Please choose an MP3 file: <input name="file" type="file" /><br>
Please choose a rendering core: <select name="core">
									<?php
										foreach(scandir('/pyBlender/Scripts/RenderingCores') as $core){
											$core = pathinfo($core, PATHINFO_FILENAME);
											echo "<option value = '" . $core . "'>" . $core . "</option>";
										}
									?>
								</select><br>
Please choose a spectrogram level: 	<select name="mels">
											<option value=5>5</option>
											<option value=6>6</option>
											<option value=7>7</option>
									</select><br>
<input type="submit" value="Begin Processing" /></form><br>
	
<script type="text/javascript" src="main.js"></script>
	
<?php
if(!file_exists("in_use")){
	
	unlink("Out.txt");
	unlink("terminate");
	
	$runFlag = !empty($_FILES["file"]);
	if ($runFlag){
	 	if ($_FILES["file"]["error"] > 0){
	 		echo "Error: " . $_FILES["file"]["error"] . "<br>";
			$runFlag = false;
	 	}
	 	else{
			if(!file_exists("in_use")){
				
				$core = $_POST['core'];
				$mels = $_POST['mels'];
				
				$sid = session_id();
				$block = fopen("in_use", "c+");
				fwrite($block, "Script is in use by SDI: ".$sid."\r\n");
				fclose($block);
				
				echo "Selected file: ".$_FILES["file"]["name"]."<br>Size: ".(int)($_FILES["file"]["size"]/1024)." kB<br>";
				move_uploaded_file($_FILES["file"]["tmp_name"],$_FILES["file"]["name"]);
				
				echo "Selected core: " . $core . "<br>";
				echo "Selected levels: " . $mels . "<br>";
				
				$file_parts = pathinfo($_FILES["file"]["name"]);
				switch($file_parts['extension'])
				{
					case "mp3":
						rename($_FILES["file"]["name"],"pyBlender\Output\userMusic.mp3");
						$cmd = 'start "PHP Daemon" "C:\Program Files (x86)\PHP\v5.3\php.exe" -f mediator.php ' . $core . " " . $mels;
						pclose(popen($cmd, 'r'));
						break;

					case "": // Handle file extension for files ending in '.'
					case NULL: // Handle no file extension
					default:
						$runFlag = false;
						unlink($_FILES["file"]["name"]);
						unlink("in_use");
						break;
				}
				
				
			}
			else{echo('Oops! Another user is in the middle of the process... Please come back in a few minutes!');}
	 	}
	}
	echo('
	
	<script>
	window.setInterval("reloadFrame();", 1000);
	function reloadFrame() {
	document.getElementById("dynamic-content").src="dynamic.php#iFrameAnchor";}
	</script>
	
	<h1>Python Web Portal - *Process is ');
	
	if($runFlag){
		echo('ACTIVE*</h1>
		<iframe id="dynamic-content" 
			width="800" 
			height="600" 
			style="background-color:#000000;" 
			scrolling="yes">
		</iframe>
		<br>
		<a href="pyBlender/Output/Final.blend" download="pyBlend.blend">DOWNLOAD YOUR FILES WHEN THEY ARE READY</a>
		</body></html>
		');
	}
	else{
		echo('WAITING*</h1><br>
		Please initiate the process, using the menu above.');
	}
	
	
}

else{
	echo('
	<h1>SITE BUSY! Come back in a few minutes and try again!</h1>
	');
}
?>