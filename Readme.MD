# search.py
## Find stocks, indices, mutual funds, futures, currency / forex / crypto using a free-form query or symbol as seen on Google Finance - https://www.google.com/finance.

# Market_trends.py
## Get the latest market trends and relevant news. Supported trends: Most Active, Gainers, Losers, Crypto, Currencies and Climate Leaders. 

# Stock Quote.py
## Get stock market quote. Supports all stock types: stock, index, mutual fund and futures.
### Batching: up to 100 symbols are supported in a single request (separated by comma, as shown in the 2nd example above). Note that every 10 symbols will be charged as a single request - for example, sending 78 symbols will be counted & charged as 8 requests.

# Stock_Time_Series 
## Get stock time series and key news events for the following periods: 1 day, 5 days, 1 month, 6 months, year-to-date, 1 year, 5 years and all times

# Stock_Company_Overview.py
## Get stock / public company details. Supports all stock types: stock, index, mutual fund and futures. Returns company details for the stock type.

# Company_Income_Statement.py
## Get public company's quarterly or annual income statement. Supports the stock type only.

# Company_Balance_Sheet.py
## Get public company's quarterly or annual balance sheet. Supports the stock type only.

# Company_Cash_Flow
## Get public company's quarterly or annual cash flow information. Supports the stock type only. 


# Stock_News.py
## Get the latest news related to a specific stock. Supports all stock types: stock, index, mutual fund and futures. 
## Output Example for Stock_news.py
```
status:"OK"
request_id:"9946141b-b8bc-4e99-a1b4-79766fd04996"
data:
symbol:"AAPL:NASDAQ"
type:"stock"
news:0:
article_title:"Buffett's first big semiconductor investment is a bet on Apple's future"
article_url:"https://www.cnbc.com/2022/11/19/buffetts-first-big-semiconductor-investment-is-a-bet-on-apples-future.html"
article_photo_url:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTm_E16XvCVCiSgCDPLSW9pGpu245GtpzQat47IgtPgE6pVjFXBGzohJTv7F0A"
source:"CNBC"
post_time_utc:"2022-11-19 12:56:34"
1:
article_title:"Apple Isn’t Recession Proof. The Stock Could Have a Tough 2023."
article_url:"https://www.barrons.com/articles/apple-stock-iphone-sales-51668818724"
article_photo_url:"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTxbW2mNBM4uiP3Vwjcz8FOvydxUPvX8idrueGs5ngDtEq_iYjkmQKnu0jDhb4"
source:"Barron's"
post_time_utc:"2022-11-19 00:47:00"
2:
article_title:"How Warren Buffett Made a Bet on Apple Without Buying More Apple Stock"
article_url:"https://www.fool.com/investing/2022/11/18/how-warren-buffett-bet-apple-without-apple-stock/"
article_photo_url:"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNjC91x5fpDQhwcWjI0M_txULcLwx4rhvI1EZJv0XRRp-1k-cFsKWTBy2coNY"
source:"The Motley Fool"
post_time_utc:"2022-11-18 12:11:00"
3:
article_title:"Chinese Government Steps In to Help an Apple iPhone Factory"
article_url:"https://www.nytimes.com/2022/11/18/business/apple-foxconn-china.html"
article_photo_url:"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQYy0msXB5s6b8xkrP2ZGfoFN-NzesNI97BCqn2TxJGLGDNMZcS_sIZFc1VOHc"
source:"The New York Times"
post_time_utc:"2022-11-18 11:44:59"
4:
article_title:"iPhone Data Changes Are Biggest Cause of Meta ($META) Woes"
article_url:"https://www.bloomberg.com/news/articles/2022-11-17/iphone-data-changes-are-biggest-cause-of-meta-meta-woes"
article_photo_url:"https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcQmsejNbUl-XtHCIx5BxbQe8hxjXI7VXEu2ltYmc3KExAifyH5QAdV_Xhku9no"
source:"Bloomberg.com"
post_time_utc:"2022-11-17 10:00:14"
5:
article_title:"Why Apple's secrecy about its metaverse plans is looking smarter every day"
article_url:"https://www.fastcompany.com/90812090/apple-strategic-silence-metaverse-vr-headset"
article_photo_url:"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcSgElq-_Axw-jDxZ9wU1-qeE4uJoeq_yEkPdW2KVXxVvdyF6RWGDEbq5VBD0v4"
source:"Fast Company"
post_time_utc:"2022-11-18 09:30:00"
6:
article_title:"Apple Shares Deadlines for Ordering Gifts in Time for the Holidays"
article_url:"https://www.macrumors.com/2022/11/17/apple-holiday-shipping-deadlines-2022/"
article_photo_url:"https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcR1-k5Iuqp2VeIv-fBTDnEkfHi8br0jPjraYVRErTb29OekuMs19FiVYmr1txM"
source:"MacRumors"
post_time_utc:"2022-11-17 15:13:57
```
