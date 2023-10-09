import requests

def send_text(message):
    token = "5909310985:AAEMJD9vTxjA2ttvIDgBvSXpIHKqt7KnOUQ"
    id = "1972570339"
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=' + message
    response = requests.get(url= url)
    response.raise_for_status()
    return response.json()

Latitude = "14.236148"
Longitude = "121.137836"
ApiKey = "71748fefc611e55935368535d4f2f954"
angela_api = "69f04e4613056b159c2761a9d9e664d2"


response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall?lat=14.236148&lon=121.137836&exclude=current,minutely,daily&appid=69f04e4613056b159c2761a9d9e664d2')
response.raise_for_status()
print(response.status_code)

data = response.json()
weather_hourly = data["hourly"][7]
print(data)
weather = weather_hourly["weather"][0]
print(weather)
if weather["main"] == "Rain":
    send_text("It's gonna rain in the next 2 hours Master. Please make sure to bring an umbrella.")
elif weather["main"] == "Thunderstorm":
    send_text("There's is a thunderstorm in the next 2 hours Master. Be prepared for the annoying noise.")
elif weather["main"] == "Clear":
    send_text("The weather is good today Master. You have an option not to bring the umbrella but still it's better to bring one.")
elif weather["main"] == "Clouds":
    send_text("The weather is gonna be cloudy in the next 2 hours Master. Therefore, there might a chance that it is going to rain. Hope you bring your umbrella today.")
elif weather["main"] == "Drizzle":
    send_text("The rain in the next 2 hours will only be drizzle Master. Prepare your umbrella.")
else:
    print("There might be an atmospheric event that will occur in the next 2 hours Master. Please be careful.")

