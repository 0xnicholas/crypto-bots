import asyncio
import time
from typing import TYPE_CHECKING, Any, Dict, List, Optional

"""
from
connector.exchange.binance import
core.data_type.order_book_tracker_data_source import OrderBookTrackerDataSource
core.web_assistant
logger
"""

class BinanceAPIOrderBookDataSource(OrderBookTrackerDataSource):

    def __init__():
        super().__init__()
        return
    
    async def _get_last_traded_price(self, trading_pairs: List[str], domain: Optional[str] = None) -> Dic[str, float]:
        return
    
    async def _request_order_book_snapshot(self, trading_pair: str) -> Dic[str, float]:
        """
        从交易所获取特定交易对的完整订单簿副本
        :param trading_pair: 要检索订单簿的交易对
        :return the response from the exchange (JSON dictionary)
        """

        return
    
    async def _subscribe_channels(self, ws: WSAssistant):
        
        raise

    async def _connected_websocket_assistant(self) -> WSAssistant:
        # ws: WSAssistant = await self._api_factory.get_ws_assistant()

        return ws
    
    async def _order_book_snapshot(self, trading_piar: str) -> OrderBookMessage:
        return
    
    async def _parsee_trade_message(self, raw_message: Dict[str, Any], message_queue: asyncio.Queue):
        #if "result" not in raw_message:
        return

    async def _parse_order_book_diff_message(self, raw_message: Dict[str, Any], message_queue: asyncio.Queue):
        # if "result" not in raw_message:
        return
    
    def _channel_originating_message(self, event_message: Dict[str, Any]) -> str:
        channel = ""
        return channel

    