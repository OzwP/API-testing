# Install the Python Requests library:
# `pip install requests`

import requests
import json
import random as rnd
import time
import funcs as fnc

names = ["John", "Stacey", "Chris", "Lenny", "Howard", "Kate", "Rose", "Monica"]
lnames = ["Smith", "Doe", "Mccoid", "Johnson", "Brown", "Williams", "Wilson", "Horner"]
countries = ["Mexico","United States","India"]
clientid = 0
tokn = ""
testEmail = ""


def send_request():
    
    clientid += 1

    month = rnd.randint(1,12)
    day = rnd.randint(1,28)
    year = rnd.randint(1990,2021)
    date = ("%s/%s/%s" %(month,day,year))

    phone = rnd.randint(1000000000,4000000000)
    nme = names[rnd.randint(0,7)]
    lnme = lnames[rnd.randint(0,7)]

    country = countries[rnd.randint(0,2)]    

    email = testEmail+"+"+nme+lnme+"@gmail.com"

    try:
        response = requests.post(
            url="https://"+subDomain+".rest.marketingcloudapis.com/interaction/v1/events",
            headers={
                "Authorization": "Bearer " + tokn,
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "EventDefinitionKey": "",
                "ContactKey": str(clientid),
                "Data": {
                    "ClientId": str(clientid),
                    "Birthdate": date,
                    "Phone": phone,
                    "FirstName": nme,
                    "LastName": lnme,
                    "Country": country,
                    "Email": email
                }
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')




# for i in range(20):
#     send_request()
#     time.sleep(3)


if __name__ == '__main__':
    fnc.menu()