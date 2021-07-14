import configparser
from functools import cached_property
from pathlib import Path

from colorama.ansi import Fore
from usrconf import Conf
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os
import colorama
from colorama import Style

# Create settings for user on first run
if not Path('settings.ini').is_file():
    Conf().saveconf()

# Construct URL, debugging only
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

# Import user parameters from settings.ini
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
        
        # Assign default parameters if no user paramters
        elif section == 'FUNCTION':            
            for sattrb, svalue in conf.items(section):                
                    entry[sattrb]=svalue
    
    # Return Params to print                        
    return entry

# Return proper caret for negative/positive value
def caret(value):
    return f'{Style.BRIGHT}{Fore.RED}▼ {value:.2f}%{Fore.WHITE}' if float(value) < 0.0 else f'{Fore.GREEN}▲ {value:.2f}%{Fore.WHITE}'

header = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY': os.environ.get('VAL_CMC_API')
}

session = Session()
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'
session.headers.update(header)    

try: 
    response = session.get(url, params=confparams())   
    statist = []    
        
    data = json.loads(response.text)
    # Get users coin request
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