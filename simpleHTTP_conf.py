CONF = {

	#server
	'host' : "challenge01.root-me.org", #can be IP or domain name
	'port' : 80,
	'https' : False, #if True, port is usually 443
	
	'method' : "POST", #Common methods are GET, POST, TRACE, HEAD.
	'url' : "/web-serveur/ch59/admin",
	'user_agent' : "Mozilla/5.0",

	#Additional headers
	'add_headers' : ["Accept-Language: en-US,en;q=0.5",
	"Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJyb2xlIjoiZ3Vlc3QifQ.4kBPNf7Y6BrtP-Y3A-vQXPY9jAh_d0E6L4IUjL65CvmEjgdTZyr2ag-TM-glH6EYKGgO3dBYbhblaPQsbeClcw"],

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