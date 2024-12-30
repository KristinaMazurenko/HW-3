import codecs
import json
import csv
import yaml

# Создаёт текстовый файл test.txt
txt_data = "Hello, World!\n"
with codecs.open('test.txt', 'w', encoding='utf-8') as file:
    file.write(txt_data)

# Создаёт JSON-файл test.json
json_data = {
    "name": "Kristina Mazurenko",
    "age": 23,
    "address": {
        "country": "Russia",
        "street": "Krasnaya",
        "city": "Krasnodar",  
    }
}
with open('test.json', 'w', encoding='utf-8') as file:
    json.dump(json_data, file, ensure_ascii=False, indent=4)
"""
:param ensure_ascii=False сохраняет символы Unicode без экранирования.
:param indent=4 форматирует JSON с отступами.
"""

# Создаёт CSV-файл test.csv
csv_data = [
    ["name", "age", "city"],
    ["Danil Smirnov", "25", "Moscow"],
    ["Varya Krylova", "30", "Sochi"]
]
with codecs.open('test.csv', 'w', encoding='windows-1251') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerows(csv_data)

# оздаёт YAML-файл test.yaml
yaml_data = {
    "name": "John Smith",
    "age": 34,
    "address": {
        "street": "123 Main St",
        "city": "Anytown",
        "state": "Anystate",
        "zip": "12345"
    }
}
with open('test.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(yaml_data, file)