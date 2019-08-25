# Определить количество различных гласных букв латинского алфавита в некотором тексте.
text = input("Введите текст: ")
glass = 'aeiouy'
n = set()
if len(text) == 0:
    print("Текст отсуствует")
else:
    for i in text:
        if i in glass:
            n.update(i)
    print(len(set(n)))
