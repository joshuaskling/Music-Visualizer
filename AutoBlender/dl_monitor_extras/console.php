
<?php
session_start();
if(!file_exists("in_use")){
	
	unlink("Out.txt");
	
	$myHTML = '
	<!DOCTYPE html><html><head>
	<meta http-equiv="Content-Type" content="text/html" charset="windows-1256" /></head>
	
	<form enctype="multipart/form-data" action="<?php echo $_SERVER[\'PHP_SELF\']; ?>" method="POST">
	Please choose a file (it doesn\'t do anything, don\'t worry): <input name="file" type="file" /><br />
	<input type="submit" value="Begin Server Test" /></form><br>
	
	<script type="text/javascript" src="main.js"></script>
	
	<script>
	window.setInterval("reloadFrame();", 1500);
	function reloadFrame() {
	document.getElementById("dynamic-content").src="dynamic.php#iFrameAnchor";}
	</script>
	
	<h1>Python Web Portal - *Process is ACTIVE*</h1>

	<iframe id="dynamic-content" 
			width="800" 
			height="600" 
			style="background-color:#000000;" 
			scrolling="yes">
	</iframe>
	<br>
	<a href="Out.txt" download="yourConsole.txt">DOWNLOAD YOUR FILES</a>
	<br>
	when finished and then
	<br>
	<div>
	<form>
		<input type="button" name="killButton" value="Clean Up After Yourself" onclick="myTerminator();" />
	</form>
	</body></html>
	';
	
	echo ($myHTML);
	
	$sid = session_id();
	$block = fopen("in_use", "c+");
	fwrite($block, "Script is in use by SDI: ".$sid."\r\n");
	fclose($block);
	
	unlink("Log.txt");
	$cmd = 'start "PHP Daemon" "C:\Program Files (x86)\PHP\v5.3\php.exe" -f mediator.php';
	pclose(popen($cmd, 'r'));
	
}

else{
	echo('
	<h1>SITE BUSY! Come back in a few minutes and try again!</h1>
	');
}

session_destroy();
?>