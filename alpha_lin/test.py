
from alpha_lin.service.AccountBalanceService import AccountBalanceService, MarketClient, CandlestickInterval


def callback(candlestick_event: 'CandlestickEvent'):
    candlestick_event.print_object()
    print("\n")

def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


def run():
    # actBalSer=AccountBalanceService()
    # balance=actBalSer.getSpotActUSDTBalance()
    # print("当前余额为："+balance)


    market_client = MarketClient()
    market_client.sub_candlestick("btcusdt,ethusdt", CandlestickInterval.MIN5, callback, error)

