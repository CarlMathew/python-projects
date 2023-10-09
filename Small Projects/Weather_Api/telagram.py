import requests
import random
# response = requests.get("https://api.telegram.org/bot5909310985:AAEMJD9vTxjA2ttvIDgBvSXpIHKqt7KnOUQ/getUpdates")
# response.raise_for_status()
token = "5889885084:AAGkGSoNe0FipzuoR67ay2dzTtyeQ9Ca4aE"
id = "6090145470"
def send_text(message):
    token = "5889885084:AAGkGSoNe0FipzuoR67ay2dzTtyeQ9Ca4aE"
    id = "6090145470"
    url = 'https://api.telegram.org/bot' + token + '/sendMessage?chat_id=' + id + '&parse_mode=Markdown&text=' + message
    response = requests.get(url= url)
    response.raise_for_status()
    return response.json()
response = requests.get(url = f'https://api.api-ninjas.com/v1/quotes?category=happiness', headers={"X-Api-Key": "yf7/sC/baI/0y60Fd/5qCQ==5UteBZl4h3gZGtC2"})
response.raise_for_status()
data = response.json()[0]
print(data)
quotes = data["quote"]
author = data["author"]

send_text(f"""
"Missing someone is not just an absence of their physical presence; 
it's a longing for their laughter, their touch, and the warmth of their soul. 
It's a bittersweet ache that reminds us of the profound impact 
they've had on our lives and how deeply they are woven into the fabric of our hearts."
""")