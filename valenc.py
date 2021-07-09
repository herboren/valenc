import configparser
from pathlib import Path
from usrconf import Conf
from colorama.ansi import Style
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os
from colorama import Fore

# Create settings for user on first run
if not Path('settings.ini').is_file():
    Conf().saveconf()

# Import user parameters from settings.ini
def confparams():    
    conf = configparser.ConfigParser()
    conf.read('settings.ini')
    entry = {}
    
    for section in conf.sections():
        # Assign user parameters if present
        #if section == 'USER':
        #    for sattrb, svalue in conf.items(section):
        #        if svalue != '' :
        #            entry[sattrb]=svalue
        
        # Assign default parameters if no user paramters
        if section == 'DEFAULT':
            print("Section: ",section)
            for sattrb, svalue in conf.items(section):
                if svalue != '' :
                    entry[sattrb]=svalue
    
    # Return Params to print                    
    print("ENTRY: ",entry)
    return entry

# Construct URL
def cnstr_url(uparam):
    url = ['https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?']

    # Add parameterized elements        
    for attr, value in uparam.items():
        if attr == 'CMC_PRO_API_KEY':
            url.append("{}={}".format(attr, os.environ.get(value)))        
        else:
            url.append("{}={}".format(attr, value))        
    
    # Return user parameterized URL    
    return '&'.join(url).replace('?&','?')

def cnstr_hdr(uparam):      
    
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?'    
    session = Session()
    header = {}  

    for attrib, value in uparam.items():
        if attrib == 'CMC_PRO_API_KEY':
            header = {
                'Accepts':'application/json',
                'X-CMC_PRO_API_KEY': os.environ.get(value)
            }

    # Update session headers
    session.headers.update(header)
    return session.get(url, params=confparams())


def getresponse(response):    
    
    try:    
        kvp = []
        
        data = json.loads(response.text)
        print(data)
        
        # Get users coin request
        #acronyms = input("Input top 5 coins separated by comma\nto search (btc,ada,dot,eth,atom): ")
        #acronyms = acronyms.split(',')

        # Lets get symbolic data compare to elements   
        for entry in data['data']:
            for el in acronyms:
                if el.upper() == entry['symbol']:                
                    kvp.append((entry['cmc_rank'],
                                entry['symbol'],
                                entry['name'],
                                entry['quote']['USD']['price'],
                                entry['quote']['USD']['percent_change_1h'],
                                entry['quote']['USD']['percent_change_24h'],
                                entry['quote']['USD']['percent_change_7d'],
                                entry['quote']['USD']['last_updated']))

        # Create string value, append changes before printing final string
        
        for a,b,c,d,e,f,g,h in kvp:   
            
            if (int(e) or int(f) or int(g) < 0): # Formatting needs ficing on Up/Down for time values
                print("Rank: #{:0>2} Name [{}]: {} Price: ${:.2f} 1h ▼: {:.2f}% 24h ▼: {:.2f}% 7d ▼: {:.2f}% Last Updated: {}".format(a,b,c,d,e,f,g,h))
            else:
                print("Rank: #{:0>2} Name [{}]: {} Price: ${:.2f} 1h ▲: {:.2f}% 24h ▲: {:.2f}% 7d ▲: {:.2f}% Last Updated: {}".format(a,b,c,d,e,f,g,h))            
    except (ConnectionError, Timeout, TooManyRedirects) as ex:
        print(ex)

print("Real URL: ", cnstr_url(confparams()))
getresponse(cnstr_hdr(confparams()))