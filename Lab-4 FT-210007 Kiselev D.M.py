nhelp = 0
while nhelp != 1:
    try:
        n = int(input('Введите кол-во сотрудников, которым нужно заказать машину '))
    except ValueError:
        print('Вы ввели не число!\nПробуйте снова\n')
    else:
        nhelp += 1
        nhelp = nhelp
a = []
b = []
d = []
itog = []
sum = 0
end = []
endend = []
k = 0
while k < 1:
    try:
        for i in range(1, n + 1):  # i - номер машины
            print(i, 'машина')
            tarif = int(input('Введите тариф цифрой руб/км для каждой машины '))
            starif = []
            starif.append(tarif)
            starif.append(i)
            b.append(starif)
        b.sort()
        # b.sort()

    except ValueError:
        print('Вы ввели не число!\nПопробуйте снова\n')
        starif = []
        b = []
    else:
        k += 1


k_1 = 0
while k_1 < 1:
    try:
        for j in range(1, n + 1):  # j - номер работника
            print(j, 'работник')
            km = int(input('Введите расстояние в километрах от работы до дома для каждого сотрудника '))
            skm = []
            skm.append(km)
            skm.append(j)
            d.append(skm)
        d.sort()
    except ValueError:
        print('Вы ввели не число!\nПопробуйте снова!\n')
        skm = []
        d = []
    else:
        k_1 += 1


while n > 0:
    maxik = max(d)
    minik = min(b)
    hind = d.index(maxik)  # индекс максимального расстояния
    bind = b.index(minik)  # индекс минимального тарифа
    kmotvet = maxik[0]
    numwork = maxik[1]  # номер работника
    tarifotv = minik[0]
    numcar = minik[1]  # номер машины

    pay = kmotvet * tarifotv
    sum += pay  # Общая сумма
    end.append(numwork)
    end.append(numcar)
    endend.append(end)
    del d[hind]
    del b[bind]
    n = n - 1

endend.sort()

if 1 > 0:

    print(end[::2])
    print(sum)
    c = sum
    e = ((((((c % 100000) % 10000) % 1000) % 100) % 10))
    d = (((((c % 100000) % 10000) % 1000) % 100) // 10)
    diskl = (((((c % 100000) % 10000) % 1000) % 100))
    s = ((((c % 100000) % 10000) % 1000) // 100)
    te = ((((c % 100000) % 10000) // 1000))
    td = ((((c % 100000) // 10000)))
    tdiskl = (c % 100000 // 1000)
    ts = (c // 100000)

    list = []

    if (ts == 1 and ((td or te) != 0)):
        list.append("Сто")
    elif (ts == 2 and ((td or te) != 0)):
        list.append("Двести")
    elif (ts == 3 and ((td or te) != 0)):
        list.append("Триста")
    elif (ts == 4 and ((td or te) != 0)):
        list.append("Четыреста")
    elif (ts == 5 and ((td or te) != 0)):
        list.append("Пятьсот")
    elif (ts == 6 and ((td or te) != 0)):
        list.append("Шестьсот")
    elif (ts == 7 and ((td or te) != 0)):
        list.append("Семьсот")
    elif (ts == 8 and ((td or te) != 0)):
        list.append("Восемьсот")
    elif (ts == 9 and ((td or te) != 0)):
        list.append("Девятьсот")
    elif (ts == 1 and td == 0 and te == 0):
        list.append("Сто тысяч")
    elif (ts == 2 and td == 0 and te == 0):
        list.append("Двести тысяч")
    elif (ts == 3 and td == 0 and te == 0):
        list.append("Триста тысяч")
    elif (ts == 4 and td == 0 and te == 0):
        list.append("Четыреста тысяч")
    elif (ts == 5 and td == 0 and te == 0):
        list.append("Пятьсот тысяч")
    elif (ts == 6 and td == 0 and te == 0):
        list.append("Шестьсот тысяч")
    elif (ts == 7 and td == 0 and te == 0):
        list.append("Семьсот тысяч")
    elif (ts == 8 and td == 0 and te == 0):
        list.append("Восемьсот тысяч")
    elif (ts == 9 and td == 0 and te == 0):
        list.append("Девятьсот тысяч")
    else:
        ts = 0

    if tdiskl == 11:
        list.append("одиннадцать тысяч")
    elif (tdiskl == 12):
        list.append("двенадцать тысяч")
    elif (tdiskl == 13):
        list.append("тринадцать тысяч")
    elif (tdiskl == 14):
        list.append("четырнадцать тысяч")
    elif (tdiskl == 15):
        list.append("пятнадцать тысяч")
    elif (tdiskl == 16):
        list.append("шестнадцать тысяч")
    elif (tdiskl == 17):
        list.append("семнадцать тысяч")
    elif (tdiskl == 18):
        list.append("восемнадцать тысяч")
    elif (tdiskl == 19):
        list.append("девятнадцать тысяч")
    else:
        tdiskl = 0

    if td == 1 and tdiskl == 0 and te == 0:
        list.append("десять тысяч ")
    elif (td == 2 and tdiskl == 0 and te == 0):
        list.append("двадцать тысяч ")
    elif (td == 3 and tdiskl == 0 and te == 0):
        list.append("тридцать тысяч ")
    elif (td == 4 and tdiskl == 0 and te == 0):
        list.append("сорок тысяч ")
    elif (td == 5 and tdiskl == 0 and te == 0):
        list.append("пятьдесят тысяч ")
    elif (td == 6 and tdiskl == 0 and te == 0):
        list.append("шестьдесят тысяч ")
    elif (td == 7 and tdiskl == 0 and te == 0):
        list.append("семьдесят тысяч ")
    elif (td == 8 and tdiskl == 0 and te == 0):
        list.append("восемьдесят тысяч ")
    elif (td == 9 and tdiskl == 0 and te == 0):
        list.append("девяносто тысяч ")
    elif td == 1 and tdiskl == 0:
        list.append("десять тысяч")
    elif (td == 2 and tdiskl == 0 and te != 0):
        list.append("двадцать")
    elif (td == 3 and tdiskl == 0 and te != 0):
        list.append("тридцать")
    elif (td == 4 and tdiskl == 0 and te != 0):
        list.append("сорок")
    elif (td == 5 and tdiskl == 0 and te != 0):
        list.append("пятьдесят")
    elif (td == 6 and tdiskl == 0 and te != 0):
        list.append("шестьдесят")
    elif (td == 7 and tdiskl == 0 and te != 0):
        list.append("семьдесят")
    elif (td == 8 and tdiskl == 0 and te != 0):
        list.append("восемьдесят")
    elif (td == 9 and tdiskl == 0 and te != 0):
        list.append("девяносто")
    else:
        td = 0

    if te == 1 and tdiskl == 0:
        list.append("одна тысяча ")
    elif (te == 2 and tdiskl == 0):
        list.append("две тысячи")
    elif (te == 3 and tdiskl == 0):
        list.append("три тысячи")
    elif (te == 4 and tdiskl == 0):
        list.append("четыре тысячи")
    elif (te == 5 and tdiskl == 0):
        list.append("пять тысяч")
    elif (te == 6 and tdiskl == 0):
        list.append("шесть тысяч")
    elif (te == 7 and tdiskl == 0):
        list.append("семь тысяч")
    elif (te == 8 and tdiskl == 0):
        list.append("восемь тысяч")
    elif (te == 9 and tdiskl == 0):
        list.append("девять тысяч")
    else:
        te = 0

    if s == 1:
        list.append("сто")
    elif (s == 2):
        list.append("двести")
    elif (s == 3):
        list.append("триста")
    elif (s == 4):
        list.append("четыреста")
    elif (s == 5):
        list.append("пятьсот")
    elif (s == 6):
        list.append("шестьсот")
    elif (s == 7):
        list.append("семьсот")
    elif (s == 8):
        list.append("восемьсот")
    elif (s == 9):
        list.append("девятьсот")
    else:
        s = 0

    if diskl == 11:
        list.append("одиннадцать")
    elif (diskl == 12):
        list.append("двенадцать")
    elif (diskl == 13):
        list.append("тринадцать")
    elif (diskl == 14):
        list.append("четырнадцать")
    elif (diskl == 15):
        list.append("пятнадцать")
    elif (diskl == 16):
        list.append("шестнадцать")
    elif (diskl == 17):
        list.append("семнадцать")
    elif (diskl == 18):
        list.append("восемнадцать")
    elif (diskl == 19):
        list.append("девятнадцать")
    else:
        diskl = 0

    if d == 1 and diskl == 0:
        list.append("десять")
    elif (d == 2 and diskl == 0):
        list.append("двадцать")
    elif (d == 3 and diskl == 0):
        list.append("тридцать")
    elif (d == 4 and diskl == 0):
        list.append("сорок")
    elif (d == 5 and diskl == 0):
        list.append("пятьдесят")
    elif (d == 6 and diskl == 0):
        list.append("шестьдесят")
    elif (d == 7 and diskl == 0):
        list.append("семьдесят")
    elif (d == 8 and diskl == 0):
        list.append("восемьдесят")
    elif (d == 9 and diskl == 0):
        list.append("девяносто ")
    else:
        d = 0

    if e == 1 and diskl == 0:
        list.append("один рубль")
    elif (e == 2 and diskl == 0):
        list.append("два рубля")
    elif (e == 3 and diskl == 0):
        list.append("три рубля")
    elif (e == 4 and diskl == 0):
        list.append("четыре рубля")
    elif (e == 5 and diskl == 0):
        list.append("пять рублей")
    elif (e == 6 and diskl == 0):
        list.append("шесть рублей")
    elif (e == 7 and diskl == 0):
        list.append("семь рублей")
    elif (e == 8 and diskl == 0):
        list.append("восемь рублей")
    elif (e == 9 and diskl == 0):
        list.append("девять рублей")
    else:
        e = 0

    if e == 0:
        print(*list, 'рублей')
    else:
        print(*list)
