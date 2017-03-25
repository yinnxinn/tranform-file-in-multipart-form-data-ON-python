import requests

#info in website 
#files = {'name': (<filename>, <file object>,<content type>, <per-part headers>)}

files={'content':(None,'123456'),
  'platform':(None,'ios'),
  'libzip':('libmsc.zip',open('C:\Users\danwang3\Desktop\libmsc.zip','rb'),'application/x-zip-compressed')
 }
 
 url=''
 
req=requests.post(url,files=files)
