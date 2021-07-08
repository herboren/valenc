# In chemsitry the valency of an and element is the
# measure of the combining capacity with other atoms,
import configparser
from param import Param
from usrconf import Conf
from colorama.ansi import Style
from requests import Request, Session, exceptions
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os, sys, getopt
from colorama import Fore


c.saveconf('yes')
if opt in ['-d']:
c.saveconf('no')
#getcoininfo(cnstr_url(arg,p))


# Construct URL
def cnstr_url(arg, params):    
    conf = configparser.ConfigParser()
    url = ['https://pro-api.<redacted>.com/v1/cryptocurrency/listings/latest?']

    if arg == '-default':
        for attr, value in vars(params).items():
            if type(value) == int:
                if (int(value) > -1):
                    url.append("{}={}".format(attr, value))
            if type(value) == str:
                if (str(value) != ''):
                    url.append("{}={}".format(attr, value))
    elif arg == '-user':
        conf.read('settings.ini')
        for sec in conf.sections():
            for attr, val in conf.items(sec):
                print(attr, " ", val)

    

    return '&'.join(url)


header = {
        'Accepts':'application/json',
        'X-CMC_PRO_API_KEY': os.environ.get('VAL_CMC_API')
}

session = Session()
session.headers.update(header)
acronyms = input("Input top 5 coins separated by comma\nto search (btc,ada,dot,eth,atom): ")
acronyms = acronyms.split(',')

try:    
    kvp = []
    response = session.get(url, params=p.parameters)
    data = json.loads(response.text)
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
    message = []
    for a,b,c,d,e,f,g,h in kvp:   
        
        if (int(e) or int(f) or int(g) < 0): # Formatting needs ficing on Up/Down for time values
            print("Rank: #{:0>2} Name [{}]: {} Price: ${:.2f} 1h ▼: {:.2f}% 24h ▼: {:.2f}% 7d ▼: {:.2f}% Last Updated: {}".format(a,b,c,d,e,f,g,h))
        else:
            print("Rank: #{:0>2} Name [{}]: {} Price: ${:.2f} 1h ▲: {:.2f}% 24h ▲: {:.2f}% 7d ▲: {:.2f}% Last Updated: {}".format(a,b,c,d,e,f,g,h))            
except (ConnectionError, Timeout, TooManyRedirects) as ex:
    print(ex)