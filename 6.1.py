"""
Из заданной строки получить список слов, у которых первая буква гласная, а вторая – согласная.
"""

import re
letter_word = input("Введите слова на любом языке: ")
abc = re.compile(r"(\b[уеыаоэяиюeyuoia][йцкнгшщзхъфвпрлджчсмтьбqwrtpsdfghjklzxcvbnm]+[0-9a-zа-яё]+)", re.I)
list_s = re.findall(abc, letter_word)
if list_s == []:
    print("Нет слов соответсвующих условию")
else:
    print(list_s)