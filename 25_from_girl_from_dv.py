def cou(n):
    num = n
    division = [] # history
    divider = 2

    while num != 1:
        if not num % divider: # True = >0, False = 0
            num = num // divider
            division.append(divider)
        else:
            divider += 1

    res = 1
    for el in set(division):
        res *= (division.count(el) + 1)

    return res - 2
k = 0

for n in range(400000000,10**10):
    m = []
    count = cou(n)
    if count > 5:
        star = 2
        for j in range (star, n//2+1):
            if n % j == 0:
                de = int(n / j)
                su = 0
                s = str(de)
                for p in range(len(s)):
                    su += int(s[p])
                if su == 20:
                    m.append(de)
                star = de + 1

            if len(m) == 6:
                print(m[5])
                print(count)
                k += 1
                break



    if k == 5:
        break

            
                