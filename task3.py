#!/usr/bin/env python3

print("Введите строку")
str = input()

count_letters = round(len(str)/2 + 0.1) 
first_part = str[:count_letters]
second_part = str[count_letters:]

print("Первая половина: ", first_part)
print("Вторая половина: ", second_part)

print("Результат")
print(second_part + first_part)
