import asyncio
from decimal import Decimal
from typing import TYPE_CHECKING, Any, Dict, List, Optional, Tuple

from bidict import bidict

"""
from

"""

class BinanceExchange(ExchangePyBase):

    def __init__():
        super().__init__

    @staticmethod
    def binance_order_type(order_type: OrderType) -> str:
        return order_type.name.upper()
    
    @staticmethod
    def to_bot_order_type(binance_type: str) -> OrderType:
        return OrderType(binance_type)

    @property
    def auth(self):
        return BinanceAuth()

    @property
    def name(self) -> str:

        return

    @property
    def domain(self):
        return

    @property
    def client_order_id_max_length(self):
        return
    
    @property
    def client_order_id_prefix(self):
        return

    @property
    def trading_rules_request_path(self):
        return

    @property
    def trading_pairs_request_path(self):
        return

    @property
    def check_network_request_path(self):
        return
    
    @property
    def trading_pairs(self):
        return
    
    @property
    def is_cancel_request_in_exchange_sync(self) -> bool:
        return True
    
    @property
    def is_trading_required(self) -> bool:
        return
    
    def supported_order_types(self):
        return
    
    async def get_all_pairs_prices(self) -> List[Dict[str, str]]:
        return pairs_prices

    def _is_request_exception_related_to_time_sync(self, request_exception: Exception):
        return

    def _is_order_not_found_during_status_update_error(self, status_update_exeception: Exception) -> bool:
        return False

    def is_order_not_found_during_cancelation_error(self, cancelation_exception: Exception) -> bool:
        return False

    def _create_web_assistants_factory(self) -> WebAssistantsFactory:
        return
    
    def _create_order_book_data_source(self) -> OrderBookTrackerDataSource:
        return
        # BinanceAPIOrderBookDataSource()
    
    def _create_user_stream_data_source(self) -> UserStreamTrackerDataSource:
        return
        # BinanceAPIUserStreamDataSource()
    
    def _get_fee():
        return
    
    async def _place_order(self, order_id: str, trading_pair: str, amount: Decimal, trade_type: TradeType, order_type: OrderType, price: Decimal, **kwargs) -> Tuple[str, float]:
        return

    async def _place_cancel(self, order_id: str, tracked_order: InFlightOrder):
        #return True
        return False
    
    async def _format_trading_rules(self, exchange_info_dict: Dict[str, Any]) -> List[TradingRule]:
        """
        Example:
        {
            "symbol": "ETHBTC",
            "baseAssetPrecision": 8,
            "quotePrecision": 8,
            "orderTypes": ["LIMIT", "MARKET"],
            "filters": [
                {
                    "filterType": "PRICE_FILTER",
                    "minPrice": "0.00000100",
                    "maxPrice": "100000.00000000",
                    "tickSize": "0.00000100"
                }, {
                    "filterType": "LOT_SIZE",
                    "minQty": "0.00100000",
                    "maxQty": "100000.00000000",
                    "stepSize": "0.00100000"
                }, {
                    "filterType": "MIN_NOTIONAL",
                    "minNotional": "0.00100000"
                }
            ]
        }
        """
        retval = []
        return retval

    async def _update_trading_fees(self):
        pass

    async def _user_stream_event_listener(self):
        """
        该功能在后台运行，持续处理用户从交易所接收到的事件流数据源接收到的事件。它不断从队列中读取事件，直到任务中断。
        接收的事件包括余额更新、订单更新和交易事件。
        """

        # async for event_message in self._iter_user_event_quene():

    async def _update_order_fills_from_trades(self):
        """
        backup
        """
    
    async def _all_trade_updates_for_order(self, order: InFlightOrder) -> List[TradeUpdate]:
        trade_updates = []

        return trade_updates
    
    async def _request_order_status(self, tracked_order: InFlightOrder) -> OrderUpdate:
        return
    
    async def _update_balances(self):
        """
        for asset_name in asset_names_to_remove:
            del ...
        """
    
    def _init_trading_pair_symbols_from_exchange_info(self, exchange_info: Dict[str, Any]):
        mapping = bidict()
        # self._set_trading_pair_symbol_map(mapping)

    
    async def _get_last_traded_price(self, trading_pair: str) -> float:
        return