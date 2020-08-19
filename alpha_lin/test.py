
from alpha_lin.service.AccountBalanceService import AccountBalanceService, MarketClient, CandlestickInterval
import time

def callback(candlestick_event: 'CandlestickEvent'):
    print(type(candlestick_event.tick.id),"\n")
    id=candlestick_event.tick.id
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(id)), candlestick_event.tick.close)
    time.sleep(5)

def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


def run():
    #获取balance
    # actBalSer=AccountBalanceService()
    # balance=actBalSer.getSpotActUSDTBalance()
    # print("当前余额为："+balance)

    #订阅Kline
    market_client = MarketClient()
    market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN5, callback, error)

    #获取kline
    # market_client = MarketClient()
    # list_obj = market_client.get_candlestick("btcusdt", CandlestickInterval.MIN5, 50)
    # for index,obj in enumerate(list_obj):
    #     if(index+1 != len(list_obj)):
    #         percent=((obj.close-list_obj[index+1].close)/list_obj[index+1].close)*100
    #         print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(obj.id)), "\t" ,'%.4f' % percent)

