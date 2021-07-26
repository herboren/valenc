import configparser, json, os
from pathlib import *
from colorama import *
from usrconf import *
from requests import *
from requests.exceptions import *

# Create settings for user on first run
if not Path('settings.ini').is_file():
    Conf().saveconf()

# Construct URN, debugging only
def cnstr_url(entry):
    url = ['https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?']

    # Add parameterized elements        
    for attr, value in entry.items():
        if attr == 'cmc_pro_api_key':
            url.append("{}={}".format(attr.upper(), os.environ.get(value)))        
        else:
            url.append("{}={}".format(attr, value))        
    
    # Return user parameterized URL    
    return '&'.join(url).replace('?&','?')

# Import user parameters from settings.ini to session response
def confparams():    
    conf = configparser.ConfigParser()
    conf.read('settings.ini')
    entry = {}
    
    for section in conf.sections():
        # Assign user parameters if present
        if section == 'USER':
            for sattrb, svalue in conf.items(section):
                if svalue != '':
                    entry[sattrb]=svalue
                elif svalue == '' and 'CMC_PRO_API_KEY' in sattrb:
                    entry[sattrb]=os.environ.get('CMC_VAL_API')

        # Assign default parameters if no user paramters
        elif section == 'FUNCTION':            
            for sattrb, svalue in conf.items(section):                
                if svalue != '':
                    entry[sattrb]=svalue
                elif svalue == '' and 'CMC_PRO_API_KEY' in sattrb:
                    entry[sattrb]=os.environ.get('CMC_VAL_API')
    
    # Return Params to print                        
    return entry

# Return proper caret for negative/positive value
def caret(value):
    return f'{Style.BRIGHT}{Fore.RED}▼ {value:.2f}%{Fore.WHITE}' if float(value) < 0.0 else f'{Fore.GREEN}▲ {value:.2f}%{Fore.WHITE}'

# Default uniform resource name
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'

# Http header to pass to server
header = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY': os.environ.get('VAL_CMC_API')
}

# Session request for authorization over TCP connection
session = Session()

# Update header for request
session.headers.update(header)    

try: 
    # Initiate response, get information from server
    response = session.get(url, params=confparams())

    # Store JSON values   
    statist = []    
        
    data = json.loads(response.text)
    # Get users coin request, unlimited coin names
    acronyms = input("Input top 5 coins separated by comma\nto search (btc,ada,dot,eth,atom): ")
    acronyms = acronyms.split(',')

    # Lets get symbolic data compare to elements   
    """
    Getting nested Entries:
    for entry in data['data']:
        entry['symbol'],
        entry['quote']['USD']['price'],
        entry['quote']['USD']['percent_change_7d'],
    """
    for entry in data['data']:
        for el in acronyms:
            if el.upper() == entry['symbol']:                
                statist.append((entry['cmc_rank'],
                    entry['symbol'],
                    entry['name'],
                    entry['quote']['USD']['price'],
                    entry['quote']['USD']['percent_change_1h'],
                    entry['quote']['USD']['percent_change_24h'],
                    entry['quote']['USD']['percent_change_7d'],
                    entry['quote']['USD']['last_updated']))

    # Create string value, append changes before printing final string            
    for a,b,c,d,e,f,g,h in statist:                   
        print(f'\nLast Updated: {h}\n  {Fore.MAGENTA}Rank: #{a:0>2}  {Fore.CYAN}[{b}]: {c}  {Fore.YELLOW}Price: ${d:.2f}\n{Fore.WHITE}   1h: {caret(e)} 24h: {caret(f)} 7d: {caret(g)}')        
except (ConnectionError, Timeout, TooManyRedirects) as ex:
    print(ex)