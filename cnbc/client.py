from __future__ import absolute_import, division, print_function

from cnbc.resources import Quote
from cnbc.util import toJSON

class Client():
    def queryQuote(self, symbol):
        return Quote.retrieve(symbol)
    
    def apply(self, symbol, requestFn, saveFn):
        return saveFn(symbol, requestFn(symbol))
    
    def save(self, symbol, data):
        toJSON(self._build_filename(symbol), data)
        return data
    
    def _build_filename(self, symbol):
        return '{}.json'.format(symbol)