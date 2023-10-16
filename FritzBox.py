import time
import requests 
URL = "http://fritz.box/tools/kids_not_allowed.lua" 
Location = "YOUR_PATH_TO_TICKET.TXT"



with open(Location) as f:
    tickets = f.read()
    
    
tickets_list = [ticket.strip() for ticket in tickets.split() if ticket.strip()]

def getTicket():
     for i in range(0, 10):
          return tickets_list.pop(0)
        
        
def main():
    while True: 
        try:
            payload = { 
                "account": "landeviceUID-13424", 
                "ticket": getTicket(),
            } 

            s = requests.session()
            time.sleep(1)
            response = s.post(URL, data=payload)
            print(response.status_code) 
        except IndexError:
            print("No more tickets")
            exit(0)

if __name__ == "__main__":
    main()
