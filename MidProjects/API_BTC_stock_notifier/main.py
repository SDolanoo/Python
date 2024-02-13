import smtplib
import requests
import datetime as dt


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        if current > previous:
            higher = f"+{round((abs(current - previous) / previous) * 100.0, 2)}"
            return higher
        else:
            lower = f"-{round((abs(current - previous) / previous) * 100.0, 2)}"
            return lower
    except ZeroDivisionError:
        return 0


TODAY = f"{dt.datetime.now():%Y-%m-%d}"
YESTERDAY = f"{(dt.datetime.now() - dt.timedelta(1)).strftime('%Y-%m-%d')}"

STOCK = "BTC"
COMPANY_NAME = "Bitcoin"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_APIKEY = "FCTKSV0BMN1LNMUX"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_APIKEY = "23ce1616469c4632a02571758e4054d7"

MY_EMAIL="malytrolll@gmail.com"
MY_PASSWORD="xxxxxxxxxxxxxxxxx"
TO_EMAIL = "sdolazinski@gmail.com"

## Get the price and price change for BTC

# alphavantage_params = {
#     "function": "DIGITAL_CURRENCY_DAILY",
#     "symbol": f"{STOCK}",
#     "market": "USD",
#     "apikey": f"{STOCK_APIKEY}"
# }
# response_stock_price = requests.get(url=f"{STOCK_ENDPOINT}", params=alphavantage_params)
# response_stock_price.raise_for_status()
#
# data = response_stock_price.json()
# today_close = data["Time Series (Digital Currency Daily)"][f"{TODAY}"]["4a. close (USD)"]
#
# yesterday_close = data["Time Series (Digital Currency Daily)"][f"{YESTERDAY}"]["4a. close (USD)"]
#
# percent_change = get_change(float(today_close), float(yesterday_close))
#
# print(f"The price change of {STOCK} was: {percent_change}")

## Get the top trending article from https://newsapi.org/docs/endpoints/everything

news_params = {
    "q": "bitcoin",
    "language": "en",
    "from": f"{TODAY}T2:00:00",
    "to": f"{TODAY}T23:00:00",
    "sortBy": "popularity",
    "pageSize": "1",
    "apiKey": f"{NEWS_APIKEY}"
}

response_news = requests.get(url=NEWS_ENDPOINT, params=news_params)
response_news.raise_for_status()
article = response_news.json()["articles"][0]

#data_news_description = response_news.json()["articles"]

print(f"Title: {article['title']}")
print(f"Description: {article['description']}")


## Send an email with stock price change, actual price and top trending article

# TESLA_UPDATE = f"dotdot"
# TESLA_ARTICLE = f"dotdot"
# message = f"Subject:Tesla stock update\n\n{TESLA_UPDATE}\n{TESLA_ARTICLE}"
#
# with smtplib.SMTP("smtp@gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=MY_EMAIL, password=MY_PASSWORD)
#     connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_EMAIL, msg=message)
