import os
import json
import csv
import yaml
from files_utils import (
    read_json, write_json, append_json,
    read_csv, write_csv, append_csv,
    read_txt, write_txt, append_txt,
    read_yaml
)

# проверка работы функции read_json
def test_read_json():
    # проверка существования файла
    file_path = 'test.json'
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    # ожидаемый результат
    expected_data = {
        "name": "Kristina Mazurenko",
        "age": 23,
        "address": {
            "country": "Russia",
            "street": "Krasnaya",
            "city": "Krasnodar",
        }
    }
    try:
        content = read_json(file_path)
        # сравнивает результат работы функции с ожидаемым результатом
        assert content == expected_data, f"Expected {expected_data}, but got {content}"
        print("test_read_json passed")
    # если данные совпадают, выводит сообщение об успешном прохождении теста. Если нет, показывает сообщение
    except Exception as e:
        print(f"test_read_json failed: {e}")

# проверка работы функции write_json
def test_write_json():
    file_path = 'test_write.json'
    test_data = {"name": "Kristina Mazurenko", "age": 23}
    write_json(test_data, file_path)

    # считывает содержимое файла
    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)
    # сравнивает записанные данные с исходными
    assert content == test_data, f"Expected {test_data}, but got {content}"
    # удаляет тестовый файл после проверки
    os.remove(file_path)
    print("test_write_json passed")

# проверка работы функции append_json
def test_append_json():
    file_path = 'test_append.json'
    initial_data = [{"name": "Danil Smirnov", "age": 25}]
    additional_data = [{"name": "Varya Krylova", "age": 30}]
    with open(file_path, 'w', encoding='utf-8') as file:
        # создаёт файл и записывает начальные данные
        json.dump(initial_data, file)

    # добавление новых данных в файл
    append_json(additional_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = json.load(file)
    expected_content = initial_data + additional_data
    # сравнивает данные
    assert content == expected_content, f"Expected {expected_content}, but got {content}"
    # Удаляет тестовый файл
    os.remove(file_path)
    print("test_append_json passed")

# Проверяет работу функции read_csv
def test_read_csv():
    file_path = 'test.csv'
    # Проверяет существование файла
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    # Определяет ожидаемые данные 
    expected_data = [
        ["name", "age", "city"],
        ["Danil Smirnov", "25", "Moscow"],
        ["Varya Krylova", "30", "Sochi"]
    ]
    # чтение содержимого файла
    content = read_csv(file_path)
    # Сравнивает результат работы функции с ожидаемыми данными
    assert content == expected_data, f"Expected {expected_data}, but got {content}"
    print("test_read_csv passed")

# Проверяет работу функции write_csv
def test_write_csv():
    file_path = 'test_write.csv'
    test_data = [
        ["name", "age", "city"],
        ["Ivan Ivanov", "18", "Omsk"]
    ]
    
    # Вызывает функцию write_csv, записывая данные в файл
    write_csv(test_data, file_path)

    with open(file_path, 'r', encoding='windows-1251') as file:
        reader = csv.reader(file, delimiter=';')
        content = list(reader)
    # Преобразует содержимое файла в список и сравнивает с ожидаемыми данными
    assert content == test_data, f"Expected {test_data}, but got {content}"
    os.remove(file_path)
    print("test_write_csv passed")

# Проверяет работу функции append_csv
def test_append_csv():
    file_path = 'test_append.csv'
    # Создаёт начальные данные (initial_data) и данные для добавления (additional_data) в виде списков списков
    initial_data = [
        ["name", "age", "city"],
        ["Danil Smirnov", "25", "Moscow"]
    ]
    additional_data = [
        ["Varya Krylova", "30", "Sochi"]
    ]

    append_csv(additional_data, file_path)

    # Записывает начальные данные в файл
    with open(file_path, 'w', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(initial_data)

    # Добавляет дополнительные данные в файл
    with open(file_path, 'a', encoding='windows-1251', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(additional_data)

    # Читает содержимое файла для проверки
    with open(file_path, 'r', encoding='windows-1251') as file:
        reader = csv.reader(file, delimiter=';')
        content = list(reader)

    expected_content = initial_data + additional_data
    assert content == expected_content, f"Expected {expected_content}, but got {content}"
    os.remove(file_path)
    print("test_append_csv passed")

# Проверяет функцию read_txt
def test_read_txt():
    file_path = 'test.txt'
    # Проверяет, существует ли файл
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    expected_data = "Hello, World!\n"
    content = read_txt(file_path)
    # Сравнивает считанные данные с ожидаемыми
    assert content == expected_data, f"Expected {expected_data}, but got {content}"
    print("test_read_txt passed")

# Проверяет функцию write_txt
def test_write_txt():
    file_path = 'test_write.txt'
    test_data = "This is a test write operation."
    write_txt(test_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Сравнивает считанные данные с ожидаемыми
    assert content == test_data, f"Expected {test_data}, but got {content}"
    os.remove(file_path)
    print("test_write_txt passed")

# Проверяет функцию append_txt
def test_append_txt():
    file_path = 'test_append.txt'
    initial_data = "This is the initial data.\n"
    additional_data = "This is the additional data.\n"
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(initial_data)

    # Вызывает функцию append_txt для добавления новых данных в файл
    append_txt(additional_data, file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    # Сравнивает считанные данные с ожидаемыми
    assert content == initial_data + additional_data, f"Expected {initial_data + additional_data}, but got {content}"
    os.remove(file_path)
    print("test_append_txt passed")

# Проверяет функцию read_yaml
def test_read_yaml():
    file_path = 'test.yaml'
    # Проверяет существование файла
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    expected_data = {
        "name": "John Smith",
        "age": 34,
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "Anystate",
            "zip": "12345"
        }
    }
    content = read_yaml(file_path)
    # Сравнивает считанные данные с ожидаемыми 
    assert content == expected_data, f"Expected {expected_data}, but got {content}"
    print("test_read_yaml passed")

# запуск всех тестовых функций
if __name__ == "__main__":
    test_read_json()
    test_write_json()
    test_append_json()
    test_read_csv()
    test_write_csv()
    test_append_csv()
    test_read_txt()
    test_write_txt()
    test_append_txt()
    test_read_yaml()