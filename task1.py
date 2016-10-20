#!/usr/bin/env python3

print("Введите строку")
str = input()

print("Результаты")
print("Вывести третий символ этой строки: ", str[2])
print("Вывести предпоследний символ этой строки: ", str[-2])
print("Вывести первые пять символов этой строки: ", str[:5])
print("Вывести всю строку, кроме последних двух символов: ", str[:-2])
print("Вывести длину данной строки: ", len(str))

even = []
not_even = []

for item in range(0, len(str)):
	if (item % 2) == 0:
		even.append(str[item])
	else:
		not_even.append(str[item])

even = ', '.join(even)
print("Вывести все символы с четными индексами: ", even)

not_even = ', '.join(not_even)
print("Вывести все символы с нечетными индексами: ", not_even)

revert_string = ""

for item in range(1, len(str) + 1):
	revert_string += str[-1 * item]

print("Вывести все символы в обратном порядке: ", revert_string)

not_even_revert = ""

for item in range(1, len(str) + 1):
	if (item % 2) == 1:
		not_even_revert += str[-1 * item]

print("Вывести все символы строки через один в обратном порядке, начиная с последнего: ", not_even_revert)
