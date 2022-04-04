from __future__ import absolute_import, division, print_function

from cnbc.resources import Quote
from cnbc.util import toJSON

class Client():
    def queryQuote(self, symbol):
        return Quote.retrieve(symbol)
    
    def apply(self, symbol, requestFn, saveFn):
        return saveFn(symbol, requestFn(symbol).data)
    
    @classmethod
    def save(cls, symbol, data):
        toJSON(cls._build_filename(symbol), data)
        return data
    
    @classmethod
    def _build_filename(cls, symbol):
        return '{}.json'.format(symbol)