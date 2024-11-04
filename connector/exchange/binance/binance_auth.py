import hashlib
import hmac
import json
from collections import OrderedDict
from typing import Any, Dict
from urllib.parse import urlencode

"""
from
connector.time_sync
core.web_assistant
"""

class BinanceAuth(AuthBase):
    def __init__(elf, api_key: str, secret_key: str, time_provider: TimeSynchronizer):
        self.api_key = api_key
        self.secret_key = secret_key
        self.time_provider = time_provider

    
    async def rest_auth(self, request: RESTRequest) -> RESTRequest:
        return request
    
    
    async def ws_auth(self, request:WSRequest) -> WSRequest:
        return request
    
    def add_auth_to_params(self, params: Dict[str, Any]):
        
        return
    
    def header_for_auth(self) -> Dict[str, str]:
        return {}
    
    def _generate_signature(self, params: Dict[str, Any]) -> str:
        return
