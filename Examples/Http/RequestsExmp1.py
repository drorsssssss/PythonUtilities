from Examples.Http.helpers import Decorators,Functions
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
from functools import partial



class SymbolStock:
    """ This class get a url and expose interface for getting stock data"""

    def __init__(self,url):
        self.url=url
        self.timeout=5
        self.max_workers = 5

    @Decorators.func_duration
    def get_stocks_data(self,*symbols):

        res_list=[]
        for symbol in symbols:
            res_list.append(Functions.get_request(self.url,symbol,self.timeout))
        return res_list

    @Decorators.func_duration
    def get_stocks_data_concurrent(self,*symbols):
        func_partial = partial(Functions.get_request,self.url,timeout=self.timeout)

        with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(func_partial,symbols)

        return list(results)


    @Decorators.func_duration
    def get_stocks_data_parallel(self,*symbols):
        func_partial = partial(Functions.get_request,self.url,timeout=self.timeout)
        with ProcessPoolExecutor(max_workers=self.max_workers) as executor:
            results = executor.map(func_partial,symbols)

        return list(results)


def main():
    url="https://financialmodelingprep.com/api/v3/stock/real-time-price/"
    symbols = ["ADBE","CRM","GOOG","AAPL","DCO"]

    stock_cls = SymbolStock(url)
    print("Sequencially")
    print(stock_cls.get_stocks_data(*symbols))
    print()
    print("Concurrently")
    print(stock_cls.get_stocks_data_concurrent(*symbols))
    print()
    print("Parallely")
    print(stock_cls.get_stocks_data_parallel(*symbols))

if __name__ == "__main__":
    main()