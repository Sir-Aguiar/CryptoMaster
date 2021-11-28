from win10toast import ToastNotifier
from datetime import datetime
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

now = datetime.now().strftime("%H:%M")

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'15',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'f04378c1-59a3-4376-8bb4-af1a9bbc4f7a',
}

session = Session()
session.headers.update(headers)


response = session.get(url, params=parameters)
data = json.loads(response.text)


for x in range(15):
  notification = ToastNotifier()
  if data['data'][x]['name'] == "Dogecoin":
    Corpo = f"""
    {data['data'][x]['name']} ({data['data'][x]['symbol']}) 
    Last price : US$ {data['data'][x]['quote']['USD']['price']:.2f} 
    Last hour change : {data['data'][x]['quote']['USD']['percent_change_1h']:.2f}%
    Last day change: {data['data'][x]['quote']['USD']['percent_change_24h']:.2f}%
    """
    notification.show_toast(now, Corpo, duration=7)
  elif data['data'][x]['name'] == "Ethereum" or data['data'][x]['name'] == "Bitcoin":
    Corpo = f"""
    {data['data'][x]['name']} ({data['data'][x]['symbol']}) 
    Last price : US$ {data['data'][x]['quote']['USD']['price']:.2f}
    Last hour change : {data['data'][x]['quote']['USD']['percent_change_1h']:.2f}%
    Last day change : {data['data'][x]['quote']['USD']['percent_change_24h']:.2f}%
    """
    notification.show_toast(now, Corpo, duration=7)
