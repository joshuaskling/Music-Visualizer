<?php

	$file = 'Queue.txt';
	$cmd = $_POST['command'];
	$command = $cmd."\n";
	file_put_contents($file, $command, FILE_APPEND | LOCK_EX);
	
?>