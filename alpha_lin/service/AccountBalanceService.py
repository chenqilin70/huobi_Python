from alpha_lin.Config import Config
from huobi.client.account import AccountClient, AccountType


class DataService:

    def __init__(self) -> None:
        super().__init__()
        account_client = AccountClient(Config.api_key, Config.secret_key)
        self.account_balance_list = account_client.get_account_balance()

    def getSpotActUSDTBalance(self):
        spot=list(filter(lambda a : a.type==AccountType.SPOT,self.account_balance_list))[0]
        return filter(lambda b : b.currency=="usdt",spot.list[0].balance)[0].balance