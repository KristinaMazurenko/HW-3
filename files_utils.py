import os
import json
import csv
import codecs
import yaml

# читает данные из JSON-файла и возвращает их
def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

# записываем данные в JSON-файл.
def write_json(data, file_path: str, encoding: str = "utf-8"):
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

# добавляем новые данные в существующий JSON-файл. Если файл не существует, создаёт новый файл с указанными данными. Если данные являются списком, добавляем новые данные. Если не списком, создаем новый список. Если файла нет, то создаем новый список
def append_json(data: list[dict], file_path: str, encoding: str = "utf-8"):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding=encoding) as file:
            existing_data = json.load(file)
        if isinstance(existing_data, list):
            existing_data.extend(data)
        else:
            existing_data = [existing_data] + data
    else:
        existing_data = data

    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(existing_data, file, ensure_ascii=False, indent=4)

"""
:param file_path: Путь к файлу.
:param encoding: Кодировка файла (по умолчанию utf-8).
:param data: Данные, которые нужно добавить в файл.
:return: Данные, считанные из файла. 
"""

# читаем данные из CSV-файла
def read_csv(file_path, delimiter=';', encoding='windows-1251'):
    data = []
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data

# записываее данные в CSV-файл, перезаписывая его содержимое
def write_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    with open(file_path, 'w', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

# добавляет данные в существующий CSV-файл. Если файла нет, он создаётся.
def append_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    with open(file_path, 'a', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

"""
:param file_path: Путь к файлу.
:param encoding: Кодировка файла (по умолчанию 'windows-1251').
:param delimiter: Разделитель полей в файле (по умолчанию ';').
:return: Данные, считанные из файла. 
"""

# читаем текст из файла
def read_txt(file_path, encoding='utf-8'):
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    return content

# записываем текст в файл
def write_txt(data, file_path, encoding='utf-8'):
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        file.write(data)

# добавляем текст в конец файла. Если файл отсутствует, создаёт его
def append_txt(data, file_path, encoding='utf-8'):
    with codecs.open(file_path, 'a', encoding=encoding) as file:
        file.write(data)

"""
:param file_path: Путь к файлу.
:param encoding: Кодировка файла (по умолчанию utf-8).
:param data: Текст для записи .
"""

# считывает данные из YAML-файла и возвращает их как объект Python
def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data

"""
:param file_path: Путь к YAML-файлу
"""