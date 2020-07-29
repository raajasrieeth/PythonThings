import requests
#study more on requests
r=requests.get("https://financialmodelingprep.com/api/company/prince/AApl")
print(r.text)#returns text in the website#need connectivity
#learn statuscode
print(r.status_code)
#to post:
urlex="www.something.com"
dataex={"val1":23,
      "val2":3,
      "val3":6
}
r2=requests.post(url=urlex,data=dataex)