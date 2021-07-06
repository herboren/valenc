# In chemsitry the valency of an and element is the
# measure of the combining capacity with other atoms,
from requests import Request, Session, exceptions
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json, os, configparser, prmtrs, colorama

p = prmtrs.Parameters()
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {}

# Get param list count
count = len(p.param_list)

# Get messages, pitch parameter to assign
for k,v in p.param_list.items():    
        print("\n({}/{}) param: {}\nDescription: {}".format(count, len(p.param_list),k,v))
        
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
        
        # Show params left to assign
        count -= 1        

# Save settings?
#usrInput = input("Would you like to save your settings?: ")
#if usrInput.lower() == 'yes' or usrInput.lower() == 'y' :
    #for k,v in parameters.items():
        #config['USER'] = { k:v }

# Save settings to present config
#with open('settings.ini', 'w') as configfile:
    #config.write(configfile)

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