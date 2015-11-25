function checkFile() {
    var xmlHttpReq = false;
    var self = this;
    // Mozilla/Safari
    if (window.XMLHttpRequest) {
        self.xmlHttpReq = new XMLHttpRequest();
    }
    // IE
    else if (window.ActiveXObject) {
        self.xmlHttpReq = new ActiveXObject("Microsoft.XMLHTTP");
    }
    self.xmlHttpReq.open('HEAD', "Out.txt", true);
    self.xmlHttpReq.onreadystatechange = function() {
        if (self.xmlHttpReq.readyState == 4) {
            if (self.xmlHttpReq.status == 200) {
                alert('the file exists');
				$conf = confirm("Terminate!");
				if($conf){
					var http = new XMLHttpRequest();
					http.open("POST", "terminator.php", true);
					http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
					http.send("");
					window.location = 'http://www.google.com';
				}
            } else if (self.xmlHttpReq.status == 404) {
                alert('the file does not exist');
				return false;
            }
        }
    }
    self.xmlHttpReq.send();
}

//checkFile('/somefile.xml');


function myCommand() {
	//var textValue = document.getElementsByName('txtbox')[0].value
	var http = new XMLHttpRequest();
	http.open("POST", "command.php", true);
	http.setRequestHeader("Content-type","application/x-www-form-urlencoded");
	var params = "command=" + textValue; 
	http.send(params);
}

function myTerminator() {
	if(checkFile()){
	}
}