<?php 

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin
   1 => array("file", "Log.txt", "a"),  // stdout
   2 => array("file", "error.txt", "a") // stderr
);


unlink("Log.txt");

$process = proc_open("cmd.exe", $descriptorspec, $pipes);

fwrite($pipes[0], " *** Ready for User *** \n");

while(!connection_aborted()){
	sleep(1);
	$file = 'Queue.txt';
	$lines = file($file);
	unlink($file);
	$commandNumber = 0;
	foreach($lines as $line){
		$commandNumber = $commandNumber + 1;
	}
	for($i=0;$i<$commandNumber;$i++){
		fwrite($pipes[0], $lines[$i]);
	}
	if(file_exists("terminate")){
		unlink("terminate");
		unlink("children.txt");
		fwrite($pipes[0], "taskkill /f /im php.exe \n");
	}
}

?>