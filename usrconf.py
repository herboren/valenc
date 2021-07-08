import configparser
from param import Param

class Conf():               

    # Create default config       
    def saveconf(self, push):
        config = configparser.ConfigParser()  
        params = Param()

        if push.lower != 'yes':
            # Write user params            
            for k,v in vars(params).items():
                config['USER'] = { k:v }
        # Save config
        with open('settings.ini', 'w') as configfile:
            config.write(configfile)