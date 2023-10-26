def kol_par():
    sum=1
    n=1
    while (sum<=4):
        n += 1
        sum += 1/n
    return n

print(kol_par())