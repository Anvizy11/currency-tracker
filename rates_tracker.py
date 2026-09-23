import json
from datetime import datetime
import requests
url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)

# Превращаем ответ в словарь Python
data = response.json()

# Достаем курс доллара, евро и юаня
usd_rate = data["Valute"]["USD"]["Value"]
eur_rate = data["Valute"]["EUR"]["Value"]
cny_rate = data["Valute"]["CNY"]["Value"]

# фиксируем время
current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

#Выводим результаты
print(f"Обновлено: {current_time}")
print(f"Текущий курс USD: {usd_rate} руб.")
print(f"Текущий курс EUR: {eur_rate} руб.")
print(f"Текущий курс CNY: {cny_rate} руб.")
# Получаем текущие дату и время в формате "ГГГГ-ММ-ДД ЧЧ:ММ"

my_rates = {
    "updated_at": current_time,
    "USD": usd_rate,
    "EUR": eur_rate,
    "CNY": cny_rate
}
with open("rates.json", "w", encoding="utf-8") as file:
    json.dump(my_rates, file, ensure_ascii=False, indent=4)

print("Файл rates.json успешно записан на диск!")   