def permu(x):
    if x == n:
        for i in a:
            print(1+i,end='')
        print()
        return
    for i in range(n):
        if check[i] == False:
            check[i] = True
            a[x] = i
            permu(x+1)
            check[i] = False
n = 3
check = [False]*n
a = [0]*n
permu(0)
