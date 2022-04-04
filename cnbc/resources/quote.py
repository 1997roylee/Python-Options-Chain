from __future__ import absolute_import, division, print_function

import requests
from cnbc.api_response import ApiResponse
from cnbc.interfaces import OptionsChain

API_ENDPOINT = "https://cdn.cboe.com/api/global/delayed_quotes/options/"

class Quote():
    def __init__(self, symbol):
        self.symbol = symbol
    
    @classmethod
    def retrieve(cls, symbol):
        if symbol is None:
            return None
        
        instance = cls(symbol)
        return instance.request()
        
    @classmethod
    def _build_instance_url(cls, symbol):
        return '{}{}.json'.format(API_ENDPOINT, symbol)
    
    def instance_url(self):
        return self._build_instance_url(self.symbol)
    
    def request(self):
        try:
            r = requests.get(self.instance_url())
            r.raise_for_status()
            return ApiResponse(r.status_code, r.headers, r.json(), OptionsChain)
        except requests.exceptions.HTTPError as err:
            raise SystemExit(err)
         