import socket, ssl
import base64, urllib.parse
import simpleHTTP_conf


print("\n=====                 SimpleHTTP                 =====")
print("===== A simple tool to make simple HTTP requests =====")
print("=====                  By Marty                  =====\n\n")

CONF = simpleHTTP_conf.CONF

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