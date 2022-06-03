import datetime
import pandas as pd
import matplotlib.pyplot as plt
from W10_modules import Stock, Bond, Investor, StockTable, BondTable
import random 
import pandas as pd
import seaborn as sns

# API
from yahoo_fin import stock_info as si
import yfinance as yf

# random n number of stocks from sp500
number_of_stocks = 10
seed = 0
sp500 = pd.DataFrame(si.tickers_sp500()) # get list of sp500 stock symbol

# Initializing
stock_table = StockTable()
investor_id = 1
investor = Investor(investor_id = investor_id, 
                    firstname = "Jack", 
                    lastname = "Hsu", 
                    street = "222 E Harvard Ave", 
                    city= "Denver", 
                    state = "CO", 
                    zip = "80808", 
                    phone = "123-456-789")

purchase_date = '2019-01-02'
current_date =  '2022-05-27' 

notes = {} # dictionary of total income, profit, current price, purchase price
historical_price = pd.DataFrame() # historical closing price of selected stocks


# get random list of stocks from sp 500
random.seed(seed)
rand_int_list = random.sample(range(0, len(sp500)), number_of_stocks)
symbols = list(sp500.loc[rand_int_list][0])


for i, symb in enumerate(symbols):
    # downlaod stock datas
    try:
        df = yf.download(symb, start= purchase_date, end= current_date, progress=False) # download stock price using API
    except:
        print(f"{symb} not available for download")

    historical_price[symb] = df["Close"] # store closing price
    df.index = df.index.map(str) # make datetime index into string for later indexing

    share_num = random.sample(range(10, 200), 1)[0] # randomly generate shares of stocks purchased
    stock = Stock(i, investor_id, symb, share_num, df.loc[purchase_date + " 00:00:00"]["Close"], df.loc['2022-05-26' + " 00:00:00"]["Close"], 2019, 1, 1)
    stock_table.add(stock)

    notes[symb] = {"num_shares" :stock.share_num, "profit": stock.profit, "current_price": stock.current_value, "purchase_price": stock.purchase_price}
    

stats = pd.DataFrame(notes).T
stats_sorted = stats.sort_values(by = ['profit'], ascending=False)

stock_table.print_data()

# PLOTTTING
sns.set_theme("notebook")
fig, ax = plt.subplots(1, 2, figsize = (20, 8))
stats_sorted["flag"] = stats_sorted["profit"] > 0
stats_sorted["profit"].plot(kind = "bar", ax = ax[0], color= stats_sorted["flag"].map({True: 'g', False: 'r'}))
ax[0].set_xlabel("Stock Symbol")
ax[0].set_ylabel("Total Profit")
ax[0].set_title("Current Price vs. Purchase Price")

historical_price.plot(ax = ax[1])
ax[1].set_xlabel("Stock Symbol")
ax[1].set_ylabel("Price")
ax[1].set_title("Historical Price");
# fig.savefig("profit_and_historical_closing.jpg") # save image
plt.show()

fig, ax = plt.subplots(figsize = (8,8))
plt.pie(stats_sorted.num_shares, labels=stats_sorted.index, autopct='%1.0f%%', );
plt.title(f"Stock Portfolio Shares percentage - total profit ${sum(stats_sorted.profit)}");
# fig.savefig("shares_percentage.jpg") # save image
plt.show()