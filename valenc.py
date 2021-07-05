# In chemsitry the valency of an and element is the
# measure of the combining capacity with other atoms,
from requests import Request, Session, exceptions
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os, pprint


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
}

header = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':os.getenv('VAL_CMC_API') # Call API VIA EnvVar
}

session = Session()
session.headers.update(header)

acronyms = "btc,ada,dot,eth,atom"
acronyms = acronyms.split(',')

try:    
    kvp = {}
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # Lets get symbolic data compare to elements   
    for entry in data['data']:
        for el in acronyms:
            if el.upper() == entry['symbol']:                
                kvp[entry['symbol']] = entry['quote']['USD']['price']                                                
    for k, v in kvp.items():
            print("Symbol: {}, Price: ${:.2f}".format(k,v))
except (ConnectionError, Timeout, TooManyRedirects) as ex:
    print(ex)
