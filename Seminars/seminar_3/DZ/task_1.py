# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 2, 4, 3, 3, 6, 7, 4, 8, 9]
new_list = set()

for i in my_list:
    count = my_list.count(i)
    if count > 1 and i not in new_list:
        new_list.append(i)

print(list(new_list))
