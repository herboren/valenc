import configparser
from param import Param

class Conf():               

    # Create default config       
    def saveconf(self):
        params = Param()
        entry = {}

        config = configparser.ConfigParser()  

        # Assign default config for basic output
        config['DEFAULT'] = {
            'start': 1,
            'limit': 10,
            'price_min': 0,
            'price_max': 100000,     
            'CMC_PRO_API_KEY': 'VAL_CMC_API'
        }

        # Write custom params            
        for attr, value in vars(params).items():
            entry[attr]=value
        
        # Assign all custom params
        config['USER'] = entry
        
        # Save config
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)