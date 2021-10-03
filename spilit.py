def splitArry(arry, n, k):
    for i in range(0, k):
        x = arry[0]
        for j in range(0, n - 1):
            arry[j] = arry[j + 1]

        arry[n - 1] = x


# main
arry = [12, 10, 5, 6, 52, 36]
n = len(arry)
position = 2

splitArry(arry, n, position)

for i in range(0, n):
    print(arry[i], end=' ')
