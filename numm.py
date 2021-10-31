
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# Driver function
list = [5,7,8,9,5,4,3,22,1,1,1,1212,22,3]
pos1, pos2 = 1, 3

print(swapPositions(list, pos1 - 1, pos2 - 1))
