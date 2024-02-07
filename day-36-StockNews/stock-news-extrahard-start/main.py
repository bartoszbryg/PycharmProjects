import time
import requests
import datetime as dt
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

API_KEY_FOR_STOCK_MARKET = "JFQKHUA5FNEL3N7G"
API_KEY_FOR_NEWS = "eee1314eb4c04130a4459c07d4619de2"

API_KEY_FOR_SMS = "ACbffd7f0385ab67bc66d979655d3f680f"
AUTH_TOKEN = "e9edb5b9c0f3bd8ef90630cbdc57ec50"
MY_TWILIO_PHONE_NUM = "+12184234816"
MY_PHONE_NUM = "+48737462400"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_FOR_STOCK_MARKET
}

response = requests.get(url="https://www.alphavantage.co/query", params=stock_params)
response.raise_for_status()
data = response.json()
print(data)
time_series_data = data["Time Series (Daily)"]

# GETTING PARTICULAR DATA FROM API
closing_price_from_yesterday = float(list(time_series_data.values())[0]["4. close"])
print(closing_price_from_yesterday)
closing_price_from_previous_day = float(list(time_series_data.values())[1]["4. close"])
print(closing_price_from_previous_day)

yesterday_date = list(time_series_data.keys())[0]
if yesterday_date != str(dt.datetime.now().date() - dt.timedelta(days=1)):
    exit()
previous_date = list(time_series_data.keys())[1]

first_date = previous_date
second_date = yesterday_date

print(first_date)
print(second_date)


# MY OBJECTIVE WAY OF PROJECT! - BEST!!!!
# SET DATE
# closing_price_from_yesterday = None
# closing_price_from_previous_day = None
#
# first_date = None
# second_date = None
#
#
# yesterday_date = dt.datetime.now() - dt.timedelta(days=1)
# yesterday_date_data = time_series_data.get(str(date_now.date()))
#
# #while closing_price_from_yesterday is None:
# #    yesterday_date_data = time_series_data.get(str(yesterday_date.date()))
# #    if yesterday_date_data is not None:
# #        second_date = yesterday_date.date()
# #        closing_price_from_yesterday = float(yesterday_date_data["4. close"])  # <----------------------------- #
# #
# #     yesterday_date = yesterday_date - dt.timedelta(days=1)
# if yesterday_date_data is not None:
#     second_date = yesterday_date.date()
#     closing_price_from_yesterday = float(yesterday_date_data["4. close"])  # <----------------------------- #
# else:
#     exit()
#
# earlier_date = yesterday_date - dt.timedelta(days=1)
# while closing_price_from_previous_day is None:
#     previous_date_data = time_series_data.get(str(earlier_date.date()))
#     if previous_date is not None:
#         first_date = earlier_date.date()
#         closing_price_from_previous_day = float(previous_date_data["4. close"])  # <----------------------------- #
#
#     earlier_date = earlier_date - dt.timedelta(days=1)
#
# print(first_date)
# print(second_date)


# STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

# CALCULATING VALUES BASED ON EXTRACTED VALUES FROM API
increase_percentage = ((closing_price_from_yesterday/closing_price_from_previous_day)-1) * 100
difference = "{:.2f}".format(abs(closing_price_from_previous_day - closing_price_from_yesterday))

# END OF FIRST PART

list_with_first_3_articles = []


# GETTING PARTICULAR DATA FROM NEWS API
def get_first_news():
    # second_date_format = second_date.split("-")
    # second_date_format = [int(value) for value in second_date_format]
    # second_date_in_dt = dt.datetime(year=second_date_format[0], month=second_date_format[1], day=second_date_format[2])
    news_params = {
        "q": COMPANY_NAME,
        "from": str((dt.datetime.now() - dt.timedelta(days=1)).date()),
        "to": str(dt.datetime.now()),
        "language": "en",
        "sortBy": "popularity",
        "apiKey": API_KEY_FOR_NEWS,
    }
    res = requests.get(url="https://newsapi.org/v2/everything", params=news_params)
    res.raise_for_status()
    articles = res.json()["articles"]
    print(articles)

    global list_with_first_3_articles
    list_with_first_3_articles = articles[:3]


# STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# SENDING SMS
def send_sms():
    global closing_price_from_yesterday, closing_price_from_previous_day
    closing_price_from_current_day = "{:.2f}".format(float(closing_price_from_yesterday))
    closing_price_from_previous_day = "{:.2f}".format(float(closing_price_from_previous_day))

    client = Client(API_KEY_FOR_SMS, AUTH_TOKEN)
    message = client.messages \
        .create(
        body=f"{STOCK}: {increase_sign}{increase_percentage}%\n"
             f"DIFFERENCE: {difference}$"
             f"\n\nYESTERDAY DATE: {second_date}\nYESTERDAY CLOSING PRICE: {closing_price_from_current_day}$"
             f"\n\nPREVIOUS CLOSING DATE: {first_date}\nPREVIOUS CLOSING PRICE: {closing_price_from_previous_day}$",
        from_=MY_TWILIO_PHONE_NUM,
        to=MY_PHONE_NUM
    )
    print(message.sid)
    print(message.status)
    time.sleep(15)
    for article in list_with_first_3_articles:
        message = client.messages \
            .create(
            body=f"{STOCK}: {increase_sign}{increase_percentage}%\n"
                 f"Headline: {article['title']}\n\nBrief: {article['description']}",
            from_=MY_TWILIO_PHONE_NUM,
            to=MY_PHONE_NUM
        )
        print(message.sid)
        print(message.status)
        time.sleep(15)


# CHECKING INCREASE PERCENTAGE
print(increase_percentage)
increase_sign = ""
increase_percentage = round(increase_percentage, 2)
if increase_percentage >= 3:
    get_first_news()
    increase_sign = "🔺"
    send_sms()
elif increase_percentage <= -3:
    get_first_news()
    increase_sign = "🔻"
    increase_percentage = abs(increase_percentage)
    send_sms()






#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

