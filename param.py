from dataclasses import dataclass
    
@dataclass
class Param:
    
    # start index of the returned paginated list
    start: str = ''
  
    # number of results to return
    limit: str = ''
  
    # threshold of minimum USD price
    price_min: str = ''
  
    # threshold of maximum USD price
    price_max: str = ''
  
    # threshold of minimum market cap
    market_cap_min: str = ''
   
    # threshold of maximum market cap
    market_cap_max: str = ''
   
    # threshold of minimum 24 hour USD volume
    volume_24h_min: str = ''
   
    # threshold of maximum 24 hour USD volume
    volume_24h_max: str = ''
   
    # threshold of minimum circulating supply
    circulating_supply_min: str = ''
   
    # threshold of maximum circulating supply
    circulating_supply_max: str = ''
    
    # threshold of minimum 24 hour percent change
    percent_change_24h_min: str = ''
    
    # threshold of maximum 24 hour percent change
    percent_change_24h_max: str = ''
    
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
    CMC_PRO_API_KEY: str = ''