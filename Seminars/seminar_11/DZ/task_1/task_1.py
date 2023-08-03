# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

import os
from time import time


class MyString(str):

    """
        Данный класс является развитием класса str, который сохраняет информацию кем и когда была создана строка
    """

    def __new__(cls, row):
        instance = super().__new__(cls, row)
        instance.user = os.getlogin()
        instance.created_time = time()
        return instance


my_str = MyString('This is testing')
print(my_str)
print(my_str.user)
print(my_str.created_time)
print(MyString.__doc__)
