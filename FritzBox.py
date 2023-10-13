import time
import requests 
URL = "http://fritz.box/tools/kids_not_allowed.lua" 
amount = 0
tickets = [
        819365,	606287,	437406,	493354,
537631,	751922,	901579,	663945,	947862,
    ]

def getTicket(amount):
    return tickets[amount]

def main():
    global amount
    while amount < 9:
        time.sleep(1)
        amount +=1
        print(amount)
        payload = { 
            "account": "landeviceUID-13424", 
            "ticket": getTicket(amount),
        } 

        s = requests.session() 
        response = s.post(URL, data=payload) 
        print(response.status_code) # If the request went Ok we usually get a 200 status. 
        print(response.text) # This is the HTML content of the page.

if __name__ == "__main__":
    main()
