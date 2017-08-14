import pandas as pd
import urllib.request

def main():
    backtest()

def backtest():
    request_url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1405699200&end=9999999999&period=300'
    data = pd.read_json(urllib.request.urlopen(request_url).read(), 'records')
    


if __name__ == "__main__": main()
