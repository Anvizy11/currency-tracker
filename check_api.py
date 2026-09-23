import requests

# Делаем реальный запрос к открытому API с курсами валют
url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)

# Превращаем ответ в словарь Python
data = response.json()

# Достаем курс доллара
usd_rate = data["Valute"]["USD"]["Value"]
print(f"Текущий курс USD: {usd_rate} руб.")