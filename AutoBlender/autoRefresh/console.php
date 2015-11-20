<?php
$cmd = 'start "PHP Daemon" "C:\Program Files (x86)\PHP\v5.3\php.exe" -f mediator.php';

pclose(popen($cmd, 'r')); 

echo('
<!DOCTYPE html><html><head></head><body>
<script type="text/javascript" src="main.js"></script>
<script>
window.setInterval("reloadIFrame();", 3000);
function reloadIFrame() {
document.getElementById("dynamic-content").src="dynamic.php#iFrameAnchor";}</script>
<h1>Win32 Process Emulator - *Process is ');

echo('ACTIVE*');

echo('
</h1>
<iframe id="dynamic-content" width="800" height="600" style="background-color:#000000;" scrolling="yes" src="dynamic.php#iFrameAnchor"></iframe>
<br>
<form>
    <input type="text" name="txtbox" />
	<input type="button" name="myButton" value="Send Command" onclick="myCommand();" />
	<input type="button" name="killButton" value="Terminate Program Space" onclick="myTerminator();" />
</form></body></html>
');

?>