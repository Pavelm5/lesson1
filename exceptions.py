def cut_cake(people):
    try:
        parts = 1 / people
        print(f'Каждый человек получит {parts} пирога')
    except ZeroDivisionError:
        print('Не надо делить на ноль!')
cut_cake(0)
