# In chemsitry the valency of an and element is the
# measure of the combining capacity with other atoms,
from requests import Request, Session, exceptions
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os, pprint


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
    'start':'1',                   # int
    'limit':'1000',                # int
    'convert':'USD',               # int
    'price_min': 0,                # int
    'price_max':100000,              # int
    #'market_cap_min':'',           # int
    #'market_cap_max':'',           # int
    #'volume_24h_min':'',           # int
    #'volume_24h_max':'',           # int
    #'circulating_supply_min':'',   # int
    #'circulating_supply_max':'',   # int
    #'percent_change_24h_min':'',   # int
    #'percent_change_24h_max':'',   # int
    #'convert':'',                  # string
    #'convert_id':'',               # string
    #'sort':'',                     # string
    #'sort_dir':'',                 # string
    #'cryptocurrency_type':'',      # string
    #'tag':'',                      # string
    #'aux':'',                      # string
}

header = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':os.getenv('VAL_CMC_API') # Call API VIA EnvVar
}

session = Session()
session.headers.update(header)

acronyms = input("Input top 5 coins separated by comma\nto search (btc,ada,dot,eth,atom): ")
acronyms = acronyms.split(',')

try:    
    kvp = []
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    # Lets get symbolic data compare to elements   
    for entry in data['data']:
        for el in acronyms:
            if el.upper() == entry['symbol']:                
                kvp.append((entry['cmc_rank'], entry['symbol'], entry['quote']['USD']['price']))

    # Show Dictionary                                          
    for r,s,p in kvp:    
            print("Rank #: {:0>2} Symbol: {}, Price: ${:.2f}".format(r,s,p))
except (ConnectionError, Timeout, TooManyRedirects) as ex:
    print(ex)
