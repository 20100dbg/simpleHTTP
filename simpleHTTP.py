import socket, ssl, base64, urllib.parse, sys, getopt
import simpleHTTP_conf

CONF = simpleHTTP_conf.CONF

try:
	opts, args = getopt.getopt(sys.argv[1:],"h:p:su:m:v", ['help', 'creds=', 'useragent=', 'get=', 'post=', 'cookie=', 'showreq=', 'showbody='])
except getopt.GetoptError as err:
	print(err)
	print('For help type : simpleHTTP.py --help')
	sys.exit(2)

for opt, arg in opts:
	if opt == "--help":
		print('simpleHTTP.py is a real simple HTTP request maker')
		print('Options : \n')
		print('-h <host>\t\tHost : sub.mydomain.com\n-p <port>\t\tDefaut : 80\n-s\t\t\tEnable HTTPS\n-u <url>\t\tPath : /folder/main\n-m <method>\t\tHTTP method : GET,POST,HEAD,etc')
		print('--creds <login:pass>\n--useragent <user agent>\tCredentials for basic HTTP auth')
		print('\nGET, POST and COOKIE data must be JSON encoded : {\'p1\':\'v1\',\'p2\':\'v2\'}')
		print('--get <data get>\t\tGET data\n--post <data post>\t\tPOST data\n--cookie <data cookie>\t\tCOOKIE data\n')
		print('--showreq\tshow request\n--showbody\tshow body response\n-v\t\tenable verbose')
		sys.exit()
	elif opt ==  ("-h"):
		CONF['host'] = arg
	elif opt ==  ("-p"):
		CONF['port'] = arg
	elif opt ==  ("-s"):
		CONF['https'] = True
	elif opt ==  ("-u"):
		CONF['url'] = arg
	elif opt ==  ("-m"):
		CONF['method'] = arg
	elif opt ==  ("--creds"):
		CONF['http_credentials'] = arg
	elif opt ==  ("--useragent"):
		CONF['user_agent'] = arg
	elif opt ==  ("--get"):
		CONF['data_get'] = arg
	elif opt ==  ("--post"):
		CONF['data_post'] = arg
	elif opt ==  ("--cookie"):
		CONF['cookie'] = arg
	elif opt ==  ("--showreq"):
		CONF['display_request'] = True
	elif opt ==  ("--showbody"):
		CONF['display_body'] = True
	elif opt ==  ("-v"):
		CONF['debug'] = True

print("\n=====                 SimpleHTTP                 =====")
print("===== A simple tool to make simple HTTP requests =====")
print("=====                  By Marty                  =====\n\n")

#Connect to socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((CONF['host'], CONF['port']))


if CONF['https']:
	context = ssl.SSLContext(ssl.PROTOCOL_TLS)
	s = ssl.wrap_socket(s)


CONF['data_get'] = urllib.parse.urlencode(CONF['data_get'])
CONF['data_post'] = urllib.parse.urlencode(CONF['data_post'])

if CONF['data_get']:
	CONF['url'] = CONF['url'] + "?" + CONF['data_get']


#Building HTTP request
req = CONF['method'] + " " + CONF['url'] + " " + "HTTP/1.1" + CONF['NEWLINE']
req = req + "Host: " + CONF['host'] + CONF['NEWLINE']
req = req + "User-Agent: " + CONF['user_agent'] + CONF['NEWLINE']
req = req + "Connection: close" + CONF['NEWLINE']

if CONF['http_credentials']:
	req = req + "Authorization: Basic " + base64.b64encode(CONF['http_credentials']) + CONF['NEWLINE']
	#req = req + "Authorization: Basic " + base64.b64encode(CONF['http_credentials'].encode('utf-8')).decode('utf-8') + CONF['NEWLINE']

if CONF['cookie']:
	req = req + "Cookie: " + urllib.parse.urlencode(CONF['cookie']).replace('&', ';') + CONF['NEWLINE']

if CONF['add_headers']:
	for h in CONF['add_headers']:
		req = req + h + CONF['NEWLINE']

#POST data is last thing in the req
if CONF['method'] == "POST" and CONF['data_post']:
	req = req + "Content-Type: application/x-www-form-urlencoded" + CONF['NEWLINE']
	req = req + "Content-Length: " + str(len(CONF['data_post'])) + CONF['NEWLINE']
	req = req + CONF['NEWLINE'] + CONF['data_post']

#end the request
req = req + CONF['NEWLINE']


if CONF['display_request']:
	print('\tREQUEST SENT\n')

	# DEBUG
	print('host : ' + CONF['host'])
	print('port : ' + str(CONF['port']))
	print('https : ' + str(CONF['https']))
	print('')

	print(req)


#send req and read the response

s.send(req.encode('utf-8'))
#s.send(req.encode('iso-8859-1'))
#python 2 : s.send(req)

r = ''

while True:
    recv = s.recv(1024)
    if not recv:
        break
    r += recv.decode('utf-8')
    #python 2 :r += recv 


if not CONF['display_body']:
	idx = r.index(CONF['NEWLINE'] + CONF['NEWLINE'])
	r = r[0:idx]

print('\n\tRESPONSE RECEIVED\n')
print(r)
print('\n\n')

s.close()