from huobi.client.account import AccountClient
from huobi.client.generic import GenericClient, CandlestickInterval
from huobi.client.market import MarketClient, LogInfo
import time
from alpha_lin.service import AccountBalanceService

def run():
    actBalSer=AccountBalanceService()
    actBalSer.getSpotActUSDTBalance()
    # print("当前余额为："+balance)
