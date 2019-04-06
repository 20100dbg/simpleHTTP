CONF = {

	#server

	#host can be IP, domain name
	'host' : "www.hackthebox.eu",
	'port' : 443,
	'https' : True,


	#remember : if https is True, port is probably 443

	#HTTP headers
	#method can be anything. Usuals GET, POST, TRACE, HEAD, or customs
	'method' : "GET",
	'url' : "/js/inviteapi.min.js",#"/api/invite/how/to/generate",

	#Credentials for htaccess type login.
	#example : 'http_credentials' : "admin:password"
	'http_credentials' : "",
	'authentification_type' : 'Basic', #supported : Basic, Digest
	'user_agent' : "Mozilla/5.0",

	#Additional headers
	'add_headers' : ["Accept-Language: en-US,en;q=0.5"],

	#get, post, cookies. example: 'data_get' : { 'login' : 'darthvader', 'password' : 'NopeImYoPapa'}
	'data_get' : {},
	'data_post' : {},
	'cookie' : {},

	#newline in HTTP requests is \r\n. Simple \n won't work with most HTTP servers
	'NEWLINE' : "\r\n",

	#Display or not the sent request. Helps to understand what's going on and debug
	'display_request' : True,
	'display_body' : True,
	'debug' : True,
}