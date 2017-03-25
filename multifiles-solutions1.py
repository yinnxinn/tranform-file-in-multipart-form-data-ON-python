# -*- coding: utf-8 -*-
import urllib2
import urllib
import time
http_url=''
key = ""
secret = ""
filepath = r""
filepath2 = r""
boundary = '----------%s' % hex(int(time.time() * 1000))
data = []
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_key')
data.append(key)
data.append('--%s' % boundary)
data.append('Content-Disposition: form-data; name="%s"\r\n' % 'api_secret')
data.append(secret)
data.append('--%s' % boundary)
fr1=open(filepath1,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr1.read())
fr.close()
data.append('--%s' % boundary)
fr2=open(filepath2,'rb')
data.append('Content-Disposition: form-data; name="%s"; filename="co33.jpg"' % 'image_file')
data.append('Content-Type: %s\r\n' % 'application/octet-stream')
data.append(fr2.read())
fr2close()
data.append('--%s--\r\n' % boundary)

http_body='\r\n'.join(data)
#buld http request
req=urllib2.Request(http_url)
#header
req.add_header('Content-Type', 'multipart/form-data; boundary=%s' % boundary)
req.add_data(http_body)
try:
	#req.add_header('Referer','http://remotserver.com/')
	#post data to server
	resp = urllib2.urlopen(req, timeout=5)
	#get response
	qrcont=resp.read()
	print qrcont

except urllib2.HTTPError as e:
    print e.read()
