# Подсчитать, из скольких разных слов состоит данное предложение.
a = input("Введите предложение: ")
punc = ['.',',',':',';','!','?','(',')']  # Список пунктуации
a = a.split()
i = 0
for word in a:
    if word[i] in punc:
        a[i] = word[:-1]
        word = a[i]
    if word[0] in punc:
        a[i] = word[i:]
i += 1
print(len(set(a)))
