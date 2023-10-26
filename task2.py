# -- coding: utf-8 --

def is_ch(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def func(x):
    if (type(x) == list):
        l2 = []
        for i in x:
            if (i not in l2):
                l2.append(i)
        return l2
    if (type(x) == dict):
        sorted_x = {}
        sorted_keys = sorted(x, key=x.get, reverse = True)
        for i in sorted_keys:
            sorted_x[i] = x[i]
        return sorted_x
    if (type(x) == int):
        if (x<2):
            return False
        i=2
        while (i <= x ** (0.5)):
            if (x%i == 0):
                return False
            i += 1
        return True



while True:
    print('Выберите какой тип данных вы хотите ввести:')
    print('1) Список.')
    print('2) Словарь.')
    print('3) Число.')
    print('4) Строка.')
    print('5) ВЫХОД.')
    ch = input()
    if (is_ch(ch) == True):
        ch = int(ch)
        if (ch == 1):
            a = []
            print('Введите количество элементов списка:')
            n = input()
            if (is_ch(n)==False):
                print("Введённое вами значение не является целым числом.")
            else:
                n = int(n)
                if (n<1):
                    print("Количество элементов должно быть положительным.")
                else:
                    print("Введите элементы списка:")
                    for i in range(n):
                        el = input()
                        a.append(el)
                    print(func(a))
        if (ch == 2):
            b={}
            print('Введите количество элементов словаря:')
            n = input()
            if (is_ch(n) == False):
                print("Введённое вами значение не является целым числом.")
            else:
                n = int(n)
                if (n < 1):
                        print("Количество элементов должно быть положительным.")
                else:
                    for i in range(n):
                        print("Введите ключ:", end = " ")
                        el_key = input()
                        print("Введите значение:", end=" ")
                        el_zn = input()
                        b.setdefault(el_key, el_zn)
                    print(func(b))
        if (ch==3):
            print('Введите число:', end = ' ')
            c = input()
            if (is_ch(c) == False):
                print("Введённое вами значение не является целым, положительным числом.")
            else:
                c=int(c)
                if (func(c) == True):
                    print("Число является простым.")
                else:
                    print("Число не является простым.")
        if (ch==4):
            print('Введите строку:', end=' ')
            d = input()
            print(d.encode('unicode_escape'))
        if (ch==5):
            print('До свидания!')
            break





