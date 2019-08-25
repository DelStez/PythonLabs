"""
Опишите, используя словарь, телефонную книгу. Составьте программу, выдающую список абонентов,
имеющих телефонный номер, начинающийся на 33.
"""
k = int(input('Введите количество номеров: '))
numbers = []
for i in range(k):
    number_of_users = []
    phone = input('Введите номер телефона в формате \'+XXXXXXXXXXXX\': ').replace('+', '')
    phone = phone.lstrip()
    number_of_users.insert(0, phone)
    if (len(number_of_users[0]) < 11) or (len(number_of_users[0]) > 12):
        print("Неверно введен номер")
        quit()
    else:
        number_of_users.insert(1, (input('Введите ФИО абонента: ')))
        numbers.append(number_of_users)

users_dict = dict(numbers)
print("Телефонная книга:", users_dict)
for key in users_dict.keys():
    i = key[0:2]
    users = []
    if i == '33':
        users.append(users_dict[key])
if not users:
    print("Номера начинающиеся на 33 отсуствуют")
else:
    print(users)
