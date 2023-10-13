import requests 
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from bs4 import BeautifulSoup 
URL = "https://fritz.box/start" 

payload = { 
            "loginView": "user", 
            "username": "backupuser",
            "uiPass": " ",
            "uiPassInput": " ",
            "PasswordInput": " ",
        } 




s = requests.session() 
retry = Retry(connect=1, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
response = s.post(URL, data=payload) 
print(response.status_code) # If the request went Ok we usually get a 200 status. 
print(response.text) # This is the HTML content of the page.






# soup = BeautifulSoup(response.content, "html.parser") 
# protected_content = soup.find(attrs={"id": "pageName"}).text 
# print(protected_content)
