import configparser

class Conf():               

    # Create default config       
    def saveconf(self):
        config = configparser.RawConfigParser()  
        # Maintains case sensitivity
        config.optionxform=str
        
        # Assign default config for basic output
        config['FUNCTION'] = {
            'start': 1,
            'limit': 10,
            'price_min': 0,
            'price_max': 100000,    
            'CMC_PRO_API_KEY':''
        }

        config['USER'] = {
            'start':'',
            'limit':'',
            'price_min':'',
            'price_max':'',
            'market_cap_min':'',
            'market_cap_max':'',
            'volume_24h_min':'',
            'volume_24h_max':'',
            'circulating_supply_min':'',
            'circulating_supply_max':'',
            'percent_change_24h_min':'',
            'percent_change_24h_max':'',
            'convert':'',
            'convert_id':'',
            'sort':'',
            'sort_dir':'',
            'cryptocurrency_type':'',
            'tag':'',
            'aux':'',     
            'CMC_PRO_API_KEY':''           
        }
        
        # Save config
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)