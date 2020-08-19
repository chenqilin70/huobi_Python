
from alpha_lin.service.AccountBalanceService import AccountBalanceService, MarketClient, CandlestickInterval
import time

def callback(candlestick_event: 'CandlestickEvent'):
    print(type(candlestick_event.tick.id),"\n")
    id=candlestick_event.tick.id
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(id)), candlestick_event.tick.close)

def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


def run():
    # actBalSer=AccountBalanceService()
    # balance=actBalSer.getSpotActUSDTBalance()
    # print("当前余额为："+balance)
    market_client = MarketClient()
    market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN5, callback, error)

