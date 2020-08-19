from huobi.client.generic import GenericClient, CandlestickInterval
from huobi.client.market import MarketClient, LogInfo
import time

def run():
    # Create generic client instance and get the timestamp
    generic_client = GenericClient()
    ts = generic_client.get_exchange_timestamp()
    s_time=time.localtime(ts)
    print(s_time)

    print(time.strftime("%Y-%m-%d %H:%M:%S", s_time))


    # Create the market client instance and get the latest btcusdt‘s candlestick
    # market_client = MarketClient()
    # list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN5, 10)
    # LogInfo.output_list(list_obj)
