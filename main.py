import random
k = random.randint(4,30)
while k!=1:
    print('В кучке', k , 'камней')
    r = int(input('Сколько вы хотите забрать камней 1, 2 или 3 \n'))
    if r <= 0 or r >= 4:
        print("Вы идёте против правил")
        exit()
    k -= r
    print('В куче осталось',k, 'камней')
    if k == 1:
        print('Вы выйграли')
        exit()
    print('Мой ход')
    if k == 4:
        r = 3
    if k == 3:
        r = 2
    if k == 2:
        r = 1
    if k > 4:
        r = random.randint(1, 3)
    k -= r
    if k == 1:
        print('Я выиграл')
        exit()