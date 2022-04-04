
from __future__ import absolute_import, division, print_function

from cnbc.interfaces.option import Option

from cnbc.interfaces.object_base import ObjectBase

class OptionsChain(ObjectBase):
    def __init__(self, payload={}):
        super()
        self.symbol = payload.get('symbol')
        self.current_price = payload.get('current_price')
        self.price_change = payload.get('price_change')
        self.price_change_percent = payload.get('price_change_percent')
        self.open = payload.get('open')
        self.high = payload.get('high')
        self.low = payload.get('low')
        self.close = payload.get('close')
        self.prev_day_close = payload.get('prev_day_close')
        self.volume = payload.get('volume')
        self.options = payload.get('options')
        self.options = list(
            map(lambda option: Option.apply(option), self.options))

    @classmethod
    def apply(cls, payload):
        return cls(payload)

    # def __dict__(self):
    #     return {
    #         'symbol': self.symbol,
    #         'current_price': self.current_price,
    #         'price_change': self.price_change,
    #         'price_change_percent': self.price_change_percent,
    #         'open': self.open,
    #         'high': self.high,
    #         'low': self.low,
    #         'close': self.close,
    #         'prev_day_close': self.prev_day_close,
    #         'volume': self.volume,
    #         'options': list(map(lambda option: option.__str__, self.options))
    #     }
