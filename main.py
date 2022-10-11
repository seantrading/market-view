import time
import datetime
import threading
import pandas as pd
import yfinance as yf

def collect_stock_info(ticker):
    global data
    ticker = ticker.replace('.', '-')
    stock = yf.Ticker(ticker)
    print("Gathering data for " + ticker)
    data += [[ticker,
             stock.info['longName'],
             stock.info['previousClose'],
             stock.info['currentPrice'],
             round((stock.info['currentPrice']-stock.info['previousClose'])/stock.info['previousClose']*100, 2)]]
    
if __name__ == "__main__":
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    wiki_data = pd.read_html(url)
    tickers = wiki_data[0]['Symbol'].tolist()

    data = []
    procs = []

    for ticker in tickers:
        proc = threading.Thread(target=collect_stock_info, args=(ticker,))
        procs.append(proc)
        proc.start()
        time.sleep(0.01)
    for proc in procs:
        proc.join()
    print("_ _ _ _ _ _ _ _ _\n")

    df = pd.DataFrame(data, columns=['Symbol', 'Name', 'Previous Close', 'Latest Price', '% Change'])
    df = df.sort_values('% Change', ascending=False)
    df['% Change'] = df['% Change'].astype(str) + '%'
    print(df)

    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    df.to_excel(r'./%s.xlsx'%date)
    print("\nExcel file downloaded\n")
    