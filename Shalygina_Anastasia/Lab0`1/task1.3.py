#Напишите программу, которая принимает от пользователя строку слов, разделённых пробелами, и сохраняет их в кортеж
# (tuple). Отобразите на экран количество уникальных слов в введённой строке. Отобразите количество гласных,
# согласных и знаков препинания в строке.

#!/usr/bin/env python3

STANDARD_DELIMITED: str = ' '

stroka: str = input(f"Введите строку слов. Используйте {STANDARD_DELIMITED}, как ' ' \n").lower()
kortezh = tuple(stroka.split())
glasnye = ['у', 'е', 'ы', 'а', 'о', 'э', 'я', 'и', 'ю','ё']
znaki = ['!', ';', ':', '?', ',', '.', '-', ' ']
kol_gl = 0
kol_sogl = 0
kol_punct = 0
colichestvo_slov = len(set(kortezh))

for sm in stroka:
    if sm in glasnye:
        kol_gl += 1
    elif sm in znaki:
        kol_punct += 1
    else:
        kol_sogl += 1

if __name__ == '__main__':

    print(f'Количество уникальных слов: {colichestvo_slov}\n')
    print(f'Количество гласных букв: {kol_gl}\n')
    print(f'Количество согласных букв: {kol_sogl}\n')
    print(f'Количество пунктуационных символов: {kol_punct}\n')



