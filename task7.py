#!/usr/bin/env python3

print("Введите строку")
str = input()

new_str = str[1: len(str) - 1]

new_str = new_str.replace('h', 'H')

print("Результат выполнения")
print(str[0] + new_str + str[len(str) - 1])
