from dataclasses import dataclass
import os
    
@dataclass
class Param:
    
    # start index of the returned paginated list
    start: int = 1
  
    # number of results to return
    limit: int = 1000
  
    # threshold of minimum USD price
    price_min: int = 0
  
    # threshold of maximum USD price
    price_max: int = 100000
  
    # threshold of minimum market cap
    market_cap_min: int = -1
   
    # threshold of maximum market cap
    market_cap_max: int = -1
   
    # threshold of minimum 24 hour USD volume
    volume_24h_min: int = -1
   
    # threshold of maximum 24 hour USD volume
    volume_24h_max: int = -1
   
    # threshold of minimum circulating supply
    circulating_supply_min: int = -1
   
    # threshold of maximum circulating supply
    circulating_supply_max: int = -1
    
    # threshold of minimum 24 hour percent change
    percent_change_24h_min: int = -1
    
    # threshold of maximum 24 hour percent change
    percent_change_24h_max: int = -1
    
    # a comma-separated list of cryptocurrency or fiat currency symbols
    # NOTE: This parameter cannot be used when convert_id is used.
    convert: str = ''
    
    # a comma-separated list of CoinMarketCap IDs
    # NOTE: This parameter cannot be used when convert is used.
    convert_id: str = ''
    
    # field to sort the list of cryptocurrencies by
    sort: str = ''
    
    # sorting direction to order cryptocurrencies
    sort_dir: str = ''
    
    # type of cryptocurrency to include
    cryptocurrency_type: str = ''
    
    # tag of cryptocurrency to include
    tag: str = ''
    
    # a comma-separated list of supplemental data fields
    aux: str = ''

    # API From Envar
    CMC_PRO_API_KEY: str = os.environ.get('VAL_CMC_API')