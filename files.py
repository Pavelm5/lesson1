with open('myfile.txt', 'r', encoding='utf-8') as myfile:
    for i in myfile:
        i = i.upper()
        i = i.replace('\n', '')
        print(i)