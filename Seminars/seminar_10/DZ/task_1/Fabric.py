# Создайте класс-фабрику.
# Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.

from Seminars.seminar_10.DZ.task_1.Animals import Horse, Bird, Fish


class Fabric:

    def __init__(self, animal_class: str,  **kwargs):
        self.animal_class = animal_class

        for key, value in kwargs.items():
            if key == 'name':
                self.name = value
            if key == 'age':
                self.age = value
            if key == 'color':
                self.color = value
            if key == 'voice':
                self.voice = value
            if key == 'power':
                self.power = value

    def get_info_animal(self):
        if self.animal_class == 'bird':
            return Bird(self.name, self.age, self.color, self.voice)
        elif self.animal_class == 'horse':
            return Horse(self.name, self.age, self.power, self.voice)
        elif self.animal_class == 'fish':
            return Fish(self.name, self.age, self.color)
        else:
            return f'нет такого животного'


if __name__ == '__main__':

    animal_1 = Fabric(animal_class='bird', name='голубь', age=2, color='белый', voice='курлык').get_info_animal()
    print(animal_1.get_info())

    animal_2 = Fabric(animal_class='horse', name='лошадь', age=8, power='галоп', voice='иииго').get_info_animal()
    print(animal_2.get_info())
