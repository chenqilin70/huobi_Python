
from  alpha_lin.service.AccountBalanceService import AccountBalanceService

def run():
    actBalSer=AccountBalanceService()
    balance=actBalSer.getSpotActUSDTBalance()
    print("当前余额为："+balance)

