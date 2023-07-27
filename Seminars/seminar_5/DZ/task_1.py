# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os

path_file = 'E:/Education/Developer/1st_quarter/Погружение в Python/Seminars/seminar_5/DZ/task_1.py'

def separation(string: str) -> tuple:
    path, filename = os.path.split(string)
    name, extension = filename.split('.')
    return path, name, extension

print(f'Исходная строка: {path_file} \nКортеж из пути: {separation(path_file)}')