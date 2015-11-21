<?php 

function terminate(){
	system('taskkill /f /im conhost.exe');
	system('taskkill /f /im php.exe');
	
}

$descriptorspec = array(
   0 => array("pipe", "r"),  // stdin
   1 => array("file", "Out.txt", "a"),  // stdout
   2 => array("file", "Err.txt", "a") // stderr
);

$process = proc_open("python pyTest.py", $descriptorspec, $pipes);
$status = proc_get_status($process);
while($status['running']==true){
	sleep(1);
	if(file_exists("terminate")){
		unlink("terminate");
		terminate();
	}
}
?>