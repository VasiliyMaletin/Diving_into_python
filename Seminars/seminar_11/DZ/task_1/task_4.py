# Доработаем класс Архив из задачи 2.
# Добавьте методы представления экземпляра для программиста
# и для пользователя.

class Archive:
    """
        Данный класс архивирует строки и числа
    """

    list_str = []
    list_int = []

    def __init__(self, int1, str1):
        self.int1 = int1
        self.str1 = str1
        self.list_int.append(int1)
        self.list_str.append(str1)

    def get_int1(self):
        return self.int1

    def get_str1(self):
        return self.str1

    @classmethod
    def get_int_arch(cls):
        return cls.list_int

    @classmethod
    def get_str_arch(cls):
        return cls.list_str

    def __str__(self):
        return f'{self.str1} {self.int1}'

    def __repr__(self):
        return f'Archive(string: "{self.str1}" number: {self.int1})'


my_archive = Archive(13, 'This is testing')
print(my_archive.__str__())
print(my_archive.__repr__())
print(Archive.__doc__)
