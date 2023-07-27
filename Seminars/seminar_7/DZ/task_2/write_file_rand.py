from random import randint, uniform


def write_file_random(filename: str, count_lines: int) -> None:
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(count_lines):
            int_num = randint(-1000, 1000)
            float_num = uniform(-1000, 1000)
            f.write(f'{int_num:>5} | {float_num:.3f}\n')


write_file_random('task_1.txt', 20)
