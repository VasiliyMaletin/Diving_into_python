def whatever():
    with (open('task_1.txt', 'r', encoding='utf-8') as f_numbers,
          open('task_2.txt', 'r', encoding='utf-8') as f_names):
        numbers = f_numbers.readlines()
        names = f_names.readlines()
    lines_to_write = []
    length_of_longest = max(len(numbers), len(names))
    for i in range(length_of_longest):
        num = numbers[i % len(numbers)]
        a, b = map(float, num.split('|'))
        mult = a * b
        name = names[i % len(names)]
        if mult >= 0:
            lines_to_write.append(f'{name.upper().rstrip()}; {round(mult)}\n')
        else:
            lines_to_write.append(f'{name.lower().rstrip()}; {abs(mult)}\n')

    with open ("task_3.txt", 'w', encoding='utf-8')as f:
        f.writelines(lines_to_write)


whatever()
