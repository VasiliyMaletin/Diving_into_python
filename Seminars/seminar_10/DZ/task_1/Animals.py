class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self) -> str:
        return f'{"Class:":8}{type(self).__name__}\n{"Name:":8}{self.name}\n{"Age:":8}{self.age} years'


class Horse(Animal):

    def __init__(self, name: str, age: int, power: str, voice: str):
        super().__init__(name, age)
        self.power = power
        self.voice = voice

    def get_info(self) -> str:
        return super().get_info() + f'\n{"Hair:":8}{self.power}\n{"Voice:":8}{self.voice}\n'


class Bird(Animal):

    def __init__(self, name: str, age: int, color: str, voice: str):
        super().__init__(name, age)
        self.color = color
        self.voice = voice

    def get_info(self) -> str:
        return super().get_info() + f'\n{"Color:":8}{self.color}\n{"Voice:":8}{self.voice}\n'


class Fish(Animal):

    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self.color = color

    def get_info(self) -> str:
        return super().get_info() + f'\n{"Color:":8}{self.color}\n'
