def is_ch(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print("Введите 2 числа:")
n = input()
m = input()
if (is_ch(n) == False or is_ch(m) == False):
    print("Необходимо ввести число.")
else:
    try:
        n = int(n)
        m = int(m)
        d = n/m
    except ZeroDivisionError as f:
        print(f)
        d=0
    finally:
        print(d)
        print("Программа закончила работу.")