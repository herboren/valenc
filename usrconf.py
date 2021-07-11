import configparser
from param import Param

class Conf():               

    # Create default config       
    def saveconf(self):
        params = Param()
        entry = {}

        config = configparser.ConfigParser()  

        # Assign default config for basic output
        config['FUNCTION'] = {
            'start': 1,
            'limit': 10,
            'price_min': 0,
            'price_max': 100000            
        }

        # Write custom params            
        for attr, value in vars(params).items():
            entry[attr]=value
        
        # Assign all custom params
        config['USER'] = entry
        
        # Save config
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)