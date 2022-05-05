#© Oswaldo Pacheco, 2022

import requests
import json
import csv
import random as rnd

subDomain = ""
tokn = ""
memberID = "ID"

names = ["John", "Stacey", "Chris", "Lenny", "Howard", "Kate", "Rose", "Monica"]
lnames = ["Smith", "Doe", "Mccoid", "Johnson", "Brown", "Williams", "Wilson", "Horner"]

testEmail = ""


def menu():

    while True:

        print("\n", "Select from the following using the number in the left")
        print("0 - Set up")
        print("1 - Request and use token")
        print("2 - Enter token manually")
        print("3 - Make .csv (coin balance)")
        print("4 - Exit")

        choice = int(input())

        if choice == 1:
            
            response = getToken()

            if response.status_code == 200:

                tokn = response.json()['access_token']

                print("Token succesfully retrived and ready to be used (only shown for reference) \n")
                print(tokn)

            else:

                print('\n', response.status_code, '\n', response.json())
        
        elif choice == 2:

            tokn = input("Enter the token to be used for authentication: ")
        
        elif choice == 3:
            print("Making .csv")
            makeCSV()
            print("Done!")
            break

        elif choice == 4:
            break
        elif choice == 0:
            setup()
        else:
            print("Enter a valid option")


        

        


def getToken():

    authUrl = "https://"+subDomain+".auth.marketingcloudapis.com/v2/token"
    
    client_id = input("Enter the client_id needed to requets the token: ")
    client_secret = input("Enter the client_secret needed to requets the token: ")

    authBody = {
        'grant_type': 'client_credentials',
        'client_id': client_id,
        'client_secret': client_secret
    }

    response = requests.post(
        url= authUrl,
        data= json.dumps(authBody)
    )

    return response



def makeCSV():

    csvName = input("Enter a name for the .csv file: ") + ".csv"

    headers = ["Loyalty_Member_Id", "First_Name", "Last_Name", "Email_Address", "zipCode", "App_Downloaded", "Coin_Balance"]

    data = [headers]

    regs = int(input("How many registries should the file contain: "))

    sID = int(input("Start id with: "))

    for i in range(regs):

        data.append(makeData(sID))
        sID += 1

    with open(csvName, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def makeData(sID):

    mID = memberID+str(sID)
    
    nme = names[rnd.randint(0,7)]
    lnme = lnames[rnd.randint(0,7)]

    atIndex = testEmail.index("@")
    
    email = testEmail[:atIndex]+"+"+nme+lnme+testEmail[atIndex:]

    zipCode = str(rnd.randint(76800, 76999))

    appDownloaded = rnd.choice([True, False])

    coinBalance = rnd.randint(0,1000)

    data = [mID, nme, lnme, email, zipCode, appDownloaded, coinBalance]
    
    return data


def setup():
    global testEmail, subDomain

    subDomain = input("Enter your SFMC subdomain: ")
    testEmail = input("Enter the email to be used for testing: ")

    