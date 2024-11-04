from decimal import Decimal
from typing import TYPE_CHECKING

from connector.exchange_base import ExchangeBase

"""
from
connector.exchange_base
core.data_type
"""

class DerivativesBase(ExchangeBase):

    def __init__(self, client_config_map: "ClientConfigAdapter"):
        super().__init__(client_config_map)
    
    def set_position_mode():
        return

    def set_leverage():
        return

    def supported_position_modes(self):
        return
    
    def get_funding_info():
        return