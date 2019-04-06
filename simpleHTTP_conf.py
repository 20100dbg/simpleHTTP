CONF = {

	#server
	'host' : "127.0.0.1", #can be IP or domain name
	'port' : 80,
	'https' : False, #if True, port is usually 443
	
	'method' : "GET", #Common methods are GET, POST, TRACE, HEAD.
	'url' : "/",
	'user_agent' : "Mozilla/5.0",

	#Additional headers
	'add_headers' : ["Accept-Language: en-US,en;q=0.5"],

	#example : {'login' : 'darthvader', 'password' : 'NopeImYoPapa'}
	'data_get' : {},
	'data_post' : {},
	'cookie' : {},

	#Credentials for htaccess type login. only supports basic
	#example : 'http_credentials' : "admin:password"
	'http_credentials' : "",

	#Display or not the sent request. Helps to understand what's going on and debug
	'display_request' : True,
	'display_body' : True,
	'debug' : True,
	'NEWLINE' : "\r\n",
}