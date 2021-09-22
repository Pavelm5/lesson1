name = ['Вася', 'Маша', 'Петя', 'Валера', 'Саша', 'Даша']

def find_person(name):
    name = input("Введите имя для поиска: ")
    while True:
        if name[0] == name:
            print('Имя', name, 'найдено')
            break
        else:    
            removed = name.pop(0)
            print(removed)
find_person(name)            



