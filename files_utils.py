import json
import os
import csv
import codecs
import yaml

def read_json(file_path: str, encoding: str = "utf-8"):
    with open(file_path, 'r', encoding=encoding) as file:
        data = json.load(file)
    return data

def write_json(data, file_path: str, encoding: str = "utf-8"):
    with open(file_path, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

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

def read_csv(file_path, delimiter=';', encoding='windows-1251'):
    data = []
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        reader = csv.reader(file, delimiter=delimiter)
        for row in reader:
            data.append(row)
    return data

def write_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    with open(file_path, 'w', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

def append_csv(data, file_path, delimiter=';', encoding='windows-1251'):
    with open(file_path, 'a', encoding=encoding, newline='') as file:
        writer = csv.writer(file, delimiter=delimiter)
        writer.writerows(data)

def read_txt(file_path, encoding='utf-8'):
    with codecs.open(file_path, 'r', encoding=encoding) as file:
        content = file.read()
    return content

def write_txt(data, file_path, encoding='utf-8'):
    with codecs.open(file_path, 'w', encoding=encoding) as file:
        file.write(data)

def append_txt(data, file_path, encoding='utf-8'):
    with codecs.open(file_path, 'a', encoding=encoding) as file:
        file.write(data)

def read_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    return data