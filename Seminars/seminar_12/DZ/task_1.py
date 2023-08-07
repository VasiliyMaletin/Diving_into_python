# Создайте класс студента.
# Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv
from functools import reduce
from pathlib import Path


def validate(value):
    if not value.isalpha():
        raise TypeError(f'Значение {value} должно содержать только буквы')
    if not value.istitle():
        raise TypeError(f'Значение {value} должно начинаться с заглавной буквы')


class Validate:

    """
        Проверка ФИО на наличие заглавных букв и составлено только из букв
    """

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        validate(value)
        setattr(instance, self.param_name, value)


class Student:
    name = Validate()
    second_name = Validate()
    surname = Validate()
    _subjects = None

    def __init__(self, name: str, second_name: str, surname: str, subjects_list: Path):
        self.name = name
        self.second_name = second_name
        self.surname = surname
        self.subjects = subjects_list

    @property
    def subjects(self):
        return self._subjects

    @subjects.setter
    def subjects(self, subjects_list: Path):

        self._subjects = {"subjects": {}}
        with open(subjects_list, 'r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                self._subjects["subjects"][row[0]] = {"assessments": [], "test_results": [], "average_test": None}
        self._subjects["middle_assessment"] = None
        self._subjects["middle_test"] = None

    def __call__(self, subject: str, number: int, type_est: str = "subject"):

        if subject not in self.subjects["subjects"].keys():
            raise AttributeError("Предмет не найден")
        if type_est == "subject":
            if number < 2 or number > 5:
                raise ValueError("Оценка должна быть от 2 до 5")
            self.subjects["subjects"][subject]["assessments"].append(number)
            self.subjects["middle_assessment"] = self.calculate_middle_estimate(self.subjects)
        elif type_est == "test":
            if number < 0 or number > 100:
                raise ValueError("Оценка должна быть от 0 до 100")
            self.subjects["subjects"][subject]["test_results"].append(number)
            self.subjects["subjects"][subject]["average_test"] = reduce(lambda x, y: x + y,
            self.subjects["subjects"][subject]["test_results"]) / len(self.subjects["subjects"][subject]["test_results"])
            self.subjects['middle_test'] = self.calculate_middle_test(self.subjects)

    @staticmethod
    def calculate_middle_estimate(subjects: dict) -> float:

        all_estimates = []
        [all_estimates.extend(subjects["subjects"][name]["assessments"]) for name in subjects["subjects"]]

        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    @staticmethod
    def calculate_middle_test(subjects: dict) -> float:

        all_estimates = []
        [all_estimates.extend(subjects["subjects"][name]["test_results"]) for name in subjects["subjects"]]

        return reduce(lambda x, y: x + y, all_estimates) / len(all_estimates)

    def __repr__(self):
        result = f'ФИО студента = {self.name} {self.second_name} {self.surname}\n' \
                 f'Средняя оценка по всем предметам = {self.subjects["middle_assessment"]}\n' \
                 f'Средний бал по всем тестам = {self.subjects["middle_test"]}\n'
        result += "\nОценки по предметам:\n"

        for key, value in self.subjects["subjects"].items():
            result += f'{key} = {value["assessments"]}\n'
        result += "\nТесты по предметам:\n"
        for key, value in self.subjects["subjects"].items():
            result += f'{key} = {value["test_results"]}, ср.бал = {value["average_test"]}\n'
        return result


if __name__ == '__main__':
    student_1 = Student("Vasiliy", "Petrovich", "Pupkin", Path('subjects_list.csv'))
    student_1("биология", 3)
    student_1("русский язык", 5)
    student_1("физика", 5)
    student_1("математика", 5)
    student_1("информатика", 35, "test")
    student_1("геометрия", 4)
    student_1("геометрия", 99, "test")
    student_1("химия", 50, "test")
    student_1("химия", 4)
    student_1("информатика", 4)
    student_1("информатика", 40, "test")
    print(student_1)

    student_2 = Student("Nikolay", "mihailovich", "Petrov", Path('subjects_list.csv'))
    student_2("русский язык", 4)
    student_2("история", 5)
    student_2("физика", 3)
    student_2("математика", 5)
    student_2("история", 40, "test")
    student_2("химия", 98, "test")
    student_2("химия", 4)
    student_2("биология", 3)
    student_2("информатика", 55, "test")
    student_2("история", 55, "test")
    print(student_2)
