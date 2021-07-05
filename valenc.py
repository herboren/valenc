# In chemsitry the valency of an and element is the
# measure of the combining capacity with other atoms,
from requests import Request, Session, exceptions
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os, pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {}
param_list = {
    'start':'(int) Optionally offset the start (1-based index) of the paginated list of items to return.',
    'limit':'(int) Optionally specify the number of results to return.',    
    'price_min':'(int) Optionally specify a threshold of minimum USD price to filter results by.',
    'price_max':'(int) Optionally specify a threshold of maximum USD price to filter results by.',
    'market_cap_min':
    '(int) Optionally specify a threshold of minimum market cap to filter results by.',
    'market_cap_max':'(int) Optionally specify a threshold of maximum market cap to filter results by.',
    'volume_24h_min':'(int) Optionally specify a threshold of minimum 24 hour USD volume to filter results by.',
    'volume_24h_max':'(int) Optionally specify a threshold of maximum 24 hour USD volume to filter results by.',
    'circulating_supply_min':'(int) Optionally specify a threshold of minimum circulating supply to filter results by.',
    'circulating_supply_max':'(int) Optionally specify a threshold of maximum circulating supply to filter results by.',
    'percent_change_24h_min':'(int) Optionally specify a threshold of minimum 24 hour percent change to filter results by.',
    'percent_change_24h_max':'(int) Optionally specify a threshold of maximum 24 hour percent change to filter results by.',
    'convert':'(string) Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated\n',
    'convert_id':'(string) Optionally calculate market quotes by CoinMarketCap ID instead of symbol. This option is identical\nto convert outside of ID format. Ex: convert_id=1,2781 would replace convert=BTC,USD in your query. This parameter cannot be used when convert is used.',
    'sort':'(string) What field to sort the list of cryptocurrencies by',
    'sort_dir':'(string) The direction in which to order cryptocurrencies against the specified sort.',
    'cryptocurrency_type':'(string) The type of cryptocurrency to include.',
    'tag':'(string) The tag of cryptocurrency to include.',
    'aux':'(string) Optionally specify a comma-separated list of supplemental data fields to return.',
}
# Get Param list count
count = len(param_list)

# Get messages, pitch parameter to assign
for k,v in param_list.items():    
        print("({}/{}) param: {}\nDescription: {}".format(count, len(param_list),k,v))
        
        # If empty input, skip param, go next
        if 'int' in v:
            inpt = input("{}: ".format(k))
            if inpt != '':
                parameters[k] = int(inpt)
            else:
                next                
        else:
            inpt = input("{}: ".format(k))
            if inpt != '':
                parameters[k] = inpt
            else:
                next
        # Clean up screen peer param description     
        os.system('cls')

        # Show params left to assign
        count -= 1        

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

# Output:
#
# (19/19) param: start
# Description: (int) Optionally offset the start (1-based index) of the paginated list of items to return.
# start: 1
#
# Input top 5 coins separated by comma
# to search (btc,ada,dot,eth,atom): btc,ada,dot,eth,atom
# Rank #: 01 Symbol: BTC, Price: $34225.44
# Rank #: 02 Symbol: ETH, Price: $2271.58
# Rank #: 05 Symbol: ADA, Price: $1.42
# Rank #: 09 Symbol: DOT, Price: $15.55
# Rank #: 31 Symbol: ATOM, Price: $12.69