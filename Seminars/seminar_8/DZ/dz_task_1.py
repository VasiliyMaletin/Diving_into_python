# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория.
# Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import csv
import json
import os
import pickle


def get_data(curr_dir: str, file_name: str):
    json_data = get_dirs_json(curr_dir)
    write_json(file_name + '.json', json_data)
    write_csv(file_name + '.pickle', json_data)


def get_dirs_json(curr_dir: str) -> dict[int:{str: str | int}]:
    dict_dir = {}
    types = ['file', 'folder']
    for i, file in enumerate(os.listdir(curr_dir), 1):
        path = os.path.join(curr_dir, file)
        item_dict = {'name': path.split('\\')[-1], 'parent': path.split('\\')[-2], 'type': None, 'size': None}
        dict_dir[i] = item_dict
        if os.path.isfile(path):
            item_dict['size'] = f'{os.path.getsize(path)} b'
            item_dict['type'] = types[0]
        elif os.path.isdir(path):
            sum_dirs = get_dir_size(path)
            print(sum_dirs)
            item_dict['size'] = f'{sum_dirs} b'
            item_dict['type'] = types[1]
            dict_dir.update(get_dirs_json(path))
    return dict_dir


def get_dir_size(path='.'):
    total = 0
    with os.scandir(path) as it:
        for entry in it:
            if entry.is_file():
                total += entry.stat().st_size
            elif entry.is_dir():
                total += get_dir_size(entry.path)
    return total


def write_json(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_csv(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow(('id', 'name', 'parent', 'type', 'size'))
        for k, v in data.items():
            writer.writerow((k, v['name'], v['parent'], v['type'], v['size']))


def write_pickle(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':
    get_data('.', 'dir_info')
