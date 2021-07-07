import configparser
from param import Param

class Conf():            
    config = configparser.ConfigParser()  

    # Create default config       
    def createusrconf(conf):
        conf['DEFAULT'] = {
            'start':'1',
            'limit':'100',
            'price_min':'0',
            'price_max':'500000'
        }
         # Save config
        with open('settings.ini', 'w') as configfile:
            conf.write(configfile)

    # Creat user config    
    def createusrconf(conf):
        params = Param()
        for k,v in vars(params).items():
                conf['USER'] = { k:v }
        # Save config
        with open('settings.ini', 'w') as configfile:
            conf.write(configfile)
