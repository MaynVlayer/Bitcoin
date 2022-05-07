import time
import sys
import os
import random
import string
import requests

def red():
    return '\u001b[31;1m'
def green():
    return '\u001b[32;1m'
def cyan():
    return '\u001b[36;1m'
def reset():
    return '\u001b[0m'
    
CYAN    = '\033[36m'
BLUE    = '\033[34m'
GREEN   = '\033[32m'
MAGENTA = '\033[35m'
RED     = '\033[31m'
RESET   = '\033[39m'


os.system("cls||clear")
def mainpass():
 print(RED + """
  ███████████   ███   █████                       ███            
 ░░███░░░░░███ ░░░   ░░███                       ░░░             
  ░███    ░███ ████  ███████    ██████   ██████  ████  ████████  
  ░██████████ ░░███ ░░░███░    ███░░███ ███░░███░░███ ░░███░░███ 
  ░███░░░░░███ ░███   ░███    ░███ ░░░ ░███ ░███ ░███  ░███ ░███ 
  ░███    ░███ ░███   ░███ ███░███  ███░███ ░███ ░███  ░███ ░███ 
  ███████████  █████  ░░█████ ░░██████ ░░██████  █████ ████ █████
 ░░░░░░░░░░░  ░░░░░    ░░░░░   ░░░░░░   ░░░░░░  ░░░░░ ░░░░ ░░░░░ 
 
 
 """)

 usernamelogin = input(GREEN + """  Username:  """)
 passwd = input(GREEN + """  Password:  """)
 passdb = requests.get("https://pastebin.com/raw/bZYmdn9j").text.splitlines()
 if passwd in passdb:
     pass
 else:
     print("""CONSOLE PASSWORD INVALID""")
     time.sleep(1)
     sys.exit()
mainpass()
os.system("cls||clear")

time.sleep(2)
print(CYAN + 'Connecting')
time.sleep(4)
print(CYAN + 'Successful connection!')
time.sleep(2)
print(CYAN + 'Loading wallets')
time.sleep(3)
print(CYAN + 'Typ start to begin')
time.sleep(1)
start = input('Typ here!')

time.sleep(2)



if start =='start': 
 def main():
   
    wallet = ('').join(random.choices(string.ascii_letters + string.digits, k=60))
    if random.randint(0,5000) < 1:
        print(GREEN + f'{wallet}' )
        time.sleep(0.009)
        print(MAGENTA + 'BTC Found: witdrawing to wallet.....')
        with open('wallet.txt', 'w') as f:
           f.writelines(wallet)
        time.sleep(6)
        sys.exit()
    else:
        print(RED + f'{wallet}')
        time.sleep(0.009)
while True:
 main()
 