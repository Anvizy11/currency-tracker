import json

# 1. Читаем JSON с диска в память
with open("rates.json", "r", encoding="utf-8") as file:
    rates_data = json.load(file)

# 2. Теперь rates_data — это полноценный словарь Python!
print("Тип данных в Python:", type(rates_data))
print("Дата из файла:", rates_data["updated_at"])

# 3. Делаем расчёт прямо в памяти:
# Считаем, сколько рублей стоят $150 по сохранённому курсу
usd = rates_data["USD"]
total_rub = 150 * usd

# 4. Модифицируем словарь в памяти: добавим новую валюту
rates_data["GBP"] = 115.50  # Британский фунт

# 5. Записываем обновлённый словарь обратно в rates.json
with open("rates.json", "w", encoding="utf-8") as file:
    json.dump(rates_data, file, ensure_ascii=False, indent=4)

print("Файл rates.json перезаписан с добавлением GBP!")