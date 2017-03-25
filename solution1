import urllib2
 
boundary='-------------------------7df3069603d6'
data=[] 
data.append('--%s' % boundary) 
data.append('Content-Disposition: form-data; name="app_id"\r\n') 
data.append('xxxxxx') 
data.append('--%s' % boundary) 
data.append('Content-Disposition: form-data; name="version"\r\n') 
data.append('xxxxx') 
data.append('--%s' % boundary) 
data.append('Content-Disposition: form-data; name="platform"\r\n') 
data.append('xxxxx') 
data.append('--%s' % boundary) 
data.append('Content-Disposition: form-data; name="libzip"; filename="C:\Users\danwang3\Desktop\libmsc.zip"') 
data.append('Content-Type: application/octet-stream\r\n') 
  
fr=open('C:\Users\danwang3\Desktop\libmsc.zip') 
content=fr.read() 
data.append(content) 
print content 
fr.close() 
data.append('--%s--\r\n'%boundary) 
httpBody='\r\n'.join(data) 
  
print type(httpBody) 
print httpBody 
  
postDataUrl='http://xxxxxxxx'
req=urllib2.Request(postDataUrl,data=httpBody) 
