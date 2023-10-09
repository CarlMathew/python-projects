import requests
from datetime import date, datetime
import html
date_now = date.today()
date_string = str(date_now).split("-")
date_yesterday = str(date(year = int(date_string[0]), month=int(date_string[1]), day=int(date_string[2]) - 2))
date_2nd_yesterday = str(date(year = int(date_string[0]), month=int(date_string[1]), day=int(date_string[2]) - 3))


new_api_key= "fc8d0778346e479b919266c8e36921a6"
news_url = f"https://newsapi.org/v2/everything?q=tesla&from=2023-04-28&sortBy=publishedAt&apiKey=fc8d0778346e479b919266c8e36921a6"
response2 = requests.get(news_url)
response2.raise_for_status()
data2 = response2.json()


title1 = data2["articles"][0]["title"]
title2 = data2["articles"][5]["title"]
title3 = data2["articles"][10]["title"]
news1 = repr(html.unescape(data2["articles"][0]["description"]))
news2 = repr(html.unescape(data2["articles"][5]["description"]))
news3 = repr(html.unescape(data2["articles"][10]["description"]))

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
my_api_key = "5VIFCGSWDTTSBREI"
url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&apikey={my_api_key}"
response = requests.get(url)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
stock_yesterday = data[date_yesterday]
stock_before_yesterday = data[date_2nd_yesterday]


def send_text(message):
    token = "5909310985:AAEMJD9vTxjA2ttvIDgBvSXpIHKqt7KnOUQ"
    id = "1972570339"
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=' + message
    response = requests.get(url= url)
    response.raise_for_status()
    return response.json()



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
status1 = stock_yesterday["4. close"]
status2 = stock_before_yesterday["4. close"]
getting_percentage = (float(status1) - float(status2)) / float(status2)
result = round(getting_percentage,4) * 100

if result < -5 or result > 2:
    print(result)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
str1 = ""

for i in news1:
    str1 += i


str2 = ""

for i in news2:
    str2 += i

str3 = ""
for i in news3:
    str3 += i

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.
send_text("TSLA: 🔺2%")
send_text(f"""
    Headline:{title2}

Brief:{str2}
    """)
if result >= 2:
    send_text(f"TSLA:🔺{result}%")
    send_text(f"""
    Headline:{title1}
    
Brief:{str1}
    """)
elif result <= -5:
    send_text(f"TSLA: 🔻{result}%")
    send_text(f"""
        Headline:{title3}

Brief:{news3}
        """)

print(str2)