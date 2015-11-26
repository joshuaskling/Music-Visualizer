<?php 

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin
   1 => array("file", "Out.txt", "a"),  // stdout
   2 => array("file", "Err.txt", "a") // stderr
);

//* PYTHON FUNCTION ONE
$process = proc_open("python pyTest.py userFile 8", $descriptorspec, $pipes);
$status = proc_get_status($process);
while($status['running']==true){
	sleep(1);
	$status = proc_get_status($process);
}
proc_close($process);
//*/


//* PYTHON FUNCTION TWO
$process = proc_open("python pyTest.py userFile 8", $descriptorspec, $pipes);
$status = proc_get_status($process);
while($status['running']==true){
	sleep(1);
	$status = proc_get_status($process);
}
proc_close($process);
//*/

//* PYTHON FUNCTION THREE
$process = proc_open("python pyTest.py userFile 8", $descriptorspec, $pipes);
$status = proc_get_status($process);
while($status['running']==true){
	sleep(1);
	$status = proc_get_status($process);
}
proc_close($process);
//*/


/* PYTHON FUNCTION FOUR
$process = proc_open("python pyTest.py arg4", $descriptorspec, $pipes);
$status = proc_get_status($process);
while($status['running']==true){
	sleep(1);
	$status = proc_get_status($process);
}
proc_close($process);
//*/

/*
blender saving through command line call, possibly? TODO

C:\Program Files\Blender Foundation\Blender>blender -P C:\Users\CoDEmanX\Desktop
\saveme.py -b C:\Users\CoDEmanX\Desktop\removeme.blend -P C:\Users\CoDEmanX\Desk
top\saveme2.py
*/

// WAITING FOR CLEANUP COMMAND OR TIMEOUT
$timer = 0;
while(true){
	sleep(1);
	$timer = $timer + 1;
	$timeout = false;
	if($timer>10){
		$timeout = true;
	}
	if(file_exists("terminate")||$timeout){
		unlink("terminate");
		unlink("in_use");
		unlink("userFile.mp3");
		$file = fopen("Out.txt", "a");
		fwrite($file, "Script terminated.");
		fclose($file);
		sleep(5);
		system('taskkill /f /im php.exe');
	}
}

?>