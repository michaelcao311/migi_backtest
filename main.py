import pandas as pd
import urllib.request
import eth.Eth as Eth

def main():
    backtest(test_fun)

def backtest(algo):
    request_url = 'https://poloniex.com/public?command=returnChartData&currencyPair=USDT_ETH&start=1405699200&end=9999999999&period=300'
    data = pd.read_json(urllib.request.urlopen(request_url).read(), 'records')
    context = Eth()

    for index, row in data.iterrows():
        context.update(data[0:index])
        algo(context)

def test_fun(eth):
    print("a")


if __name__ == "__main__": main()
