
def rotate(arry, nat, dave):
    temp = []
    issy = 0
    while (issy < dave):
        temp.append(arry[issy])
        issy = issy + 1
    issy = 0
    while (dave < nat):
        arry[issy] = arry[dave]
        issy = issy + 1
        dave = dave + 1
    arry[:] = arry[: issy] + temp
    return arry



arry = [1, 2, 3, 4, 5, 6, 7]
print("Array after left rotation is: ", end=' ')
print(rotate(arry, len(arry), 2))
