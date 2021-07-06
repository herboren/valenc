import json, os, configparser

class Parameters():
    
    config = configparser.ConfigParser()
    # Create default config
    config['DEFAULT'] = {
        'start':'1',
        'limit':'100',
        'price_min':'0',
        'price_max':'500000'
    }

    # Parameter Help
    param_list = {
        'start':'(int) Optionally offset the start (1-based index) of the paginated list of items to return.',
        'limit':'(int) Optionally specify the number of results to return.',    
        'price_min':'(int) Optionally specify a threshold of minimum USD price to filter results by.',
        'price_max':'(int) Optionally specify a threshold of maximum USD price to filter results by.',
        'market_cap_min':'(int) Optionally specify a threshold of minimum market cap to filter results by.',
        'market_cap_max':'(int) Optionally specify a threshold of maximum market cap to filter results by.',
        'volume_24h_min':'(int) Optionally specify a threshold of minimum 24 hour USD volume to filter results by.',
        'volume_24h_max':'(int) Optionally specify a threshold of maximum 24 hour USD volume to filter results by.',
        'circulating_supply_min':'(int) Optionally specify a threshold of minimum circulating supply to filter results by.',
        'circulating_supply_max':'(int) Optionally specify a threshold of maximum circulating supply to filter results by.',
        'percent_change_24h_min':'(int) Optionally specify a threshold of minimum 24 hour percent change to filter results by.',
        'percent_change_24h_max':'(int) Optionally specify a threshold of maximum 24 hour percent change to filter results by.',
        'convert':'(string) Optionally calculate market quotes in up to 120 currencies at once by passing a comma-separated',
        'convert_id':'(string) Optionally calculate market quotes by CoinMarketCap ID instead of symbol.',
        'sort':'(string) What field to sort the list of cryptocurrencies by',
        'sort_dir':'(string) The direction in which to order cryptocurrencies against the specified sort.',
        'cryptocurrency_type':'(string) The type of cryptocurrency to include.',
        'tag':'(string) The tag of cryptocurrency to include.',
        'aux':'(string) Optionally specify a comma-separated list of supplemental data fields to return.',
    }

    # Save config
#with open('settings.ini', 'w') as configfile:
    #config.write(configfile)