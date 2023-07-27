# Напишите программу, которая принимает две строки вида “a/b”
# - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction

fraction_1 = input("Введите первую дробь в формате '3/4': ")
fraction_2 = input("Введите пвторую дробь в формате '3/4': ")
temp_fraction_1 = fraction_1.split("/")
temp_fraction_2 = fraction_2.split("/")
numerator_1, denominator_1 = temp_fraction_1[0], temp_fraction_1[1]
numerator_2, denominator_2 = temp_fraction_2[0], temp_fraction_2[1]

result_1 = (int(numerator_1) / int(denominator_1)) + (int(numerator_2) / int(denominator_2))
result_2 = (int(numerator_1) / int(denominator_1)) * (int(numerator_2) / int(denominator_2))
print(result_1)
print(result_2)

fraction_check_1 = Fraction(fraction_1)
fraction_check_2 = Fraction(fraction_2)
result_3 = fraction_check_1 + fraction_check_2
result_4 = fraction_check_1 * fraction_check_2
print(result_3)
print(result_4)

