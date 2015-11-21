<?php
session_start();
?>
<!DOCTYPE html>
<html><head><meta http-equiv="Content-Type" content="text/html" charset="windows-1256" /></head><body>
<form enctype="multipart/form-data" action="<?php echo $_SERVER['PHP_SELF']; ?>" method="POST">
Please choose a file (it doesn't do anything, don't worry): <input name="file" type="file" /><br />
<input type="submit" value="Begin Server Test" /></form><br>

<?php

unlink("Log.txt");
$cmd = 'start "PHP Daemon" "C:\Program Files (x86)\PHP\v5.3\php.exe" -f mediator.php';
pclose(popen($cmd, 'r'));

echo('
<!DOCTYPE html><html><head></head><body>
<script type="text/javascript" src="main.js"></script>
<script>
window.setInterval("reloadIFrame();", 1500);
function reloadIFrame() {
document.getElementById("dynamic-content").src="dynamic.php#iFrameAnchor";}</script>
<h1>Python Web Portal - *Process is ');

echo('ACTIVE*');

echo('
</h1>
<iframe id="dynamic-content" width="800" height="600" style="background-color:#000000;" scrolling="yes"></iframe>
<br>
<form>
    <input type="text" name="txtbox" />
	<input type="button" name="myButton" value="Send Command" onclick="myCommand();" />
	<input type="button" name="killButton" value="Terminate Program Space" onclick="myTerminator();" />
</form></body></html>
');

?>