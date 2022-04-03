from __future__ import absolute_import, division, print_function

from cnbc.interfaces.object_base import ObjectBase

class Option(ObjectBase):
    def __init__(self, payload = {}):
        super()
        self.option = payload.get('option')
        self.iv = payload.get('iv')
        self.open_interest = payload.get('open_interest')
        self.volume = payload.get('volume')
        self.delta = payload.get('delta')
        self.gamma = payload.get('gamma')
        self.theta = payload.get('theta')
        self.rho = payload.get('rho')
        self.vega = payload.get('vega')
        self.theo = payload.get('theo')
        self.change = payload.get('change')
        self.open = payload.get('open')
        self.high = payload.get('high')
        self.low = payload.get('low')
        self.prev_day_close = payload.get('prev_day_close')
        
    @classmethod
    def apply(cls, payload):
        return cls(payload)
    

        
        