var http = require('http'); 
//now the application has access to http module and is able to create a server


//createServer() method is used to create an HTTP server

//create a server object
http.createServer(function(req, res){ 	

	//To display content as HTML, we include an HTTP header 
	//First Argument (200) is status code. 200 means it is ok
	//Second Argument is an object containing the response headers
	res.writeHead(200, {'Content-Type':'text/html'});
	res.end('Hello World'); //ends the reponse with the text 'hello world'
}).listen(8080); //server listens at the port '8080'