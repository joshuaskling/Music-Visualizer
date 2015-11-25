<?php 

function terminate(){
	unlink("terminate");
	unlink("in_use");
	$file = fopen("Out.txt", "w");
	fwrite($file, "Script terminated.");
	fclose($file);
	sleep(5);
	//system('taskkill /f /im conhost.exe');
	system('taskkill /f /im php.exe');
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin
   1 => array("file", "Out.txt", "a"),  // stdout
   2 => array("file", "Err.txt", "a") // stderr
);

$process = proc_open("python pyTest.py", $descriptorspec, $pipes);
$status = proc_get_status($process);
while(true){
	sleep(1);
	$status = proc_get_status($process);
	if(file_exists("terminate")){
		terminate();
	}
}
?>