def is_ch(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

print('Введите размер матрицы:')
n = input()
m = input()
if (is_ch(n) == False or is_ch(m) == False):
    print("Размер матрицы должен быть целым, положительным числом.")
else:
    n = int(n)
    m = int(m)
    arr = []
    print("Введите матрицу:")
    for i in range(n):
        arr.append([])
        str = input().split()
        for j in str:
            if (is_ch(j)==False):
                print("Элемент матрицы должен быть целым числом.")
                exit()
        arr[i]=list(map(int, str))
        if (len(arr[i])!=m):
            print("Длина строки должна быть -", m, "символов.")
            exit()
    s=0
    for i in range(n):
        if (all(x < 0 for x in arr[i]) == True):
            s = sum(arr[i])
            break
    if (s!=0):
        print(s)
    else:
        print("В матрице нет отрицательных строк.")