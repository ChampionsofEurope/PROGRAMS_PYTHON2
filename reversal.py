
def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1


def leftRotattre(arrr, de):
    n = len(arrr)
    rverseArray(arrr, 0, de - 1)
    rverseArray(arrr, de, n - 1)
    rverseArray(arrr, 0, n - 1)



def printrArray(arrr):
    for i in range(0, len(arrr)):
        print(arrr[i])


# Driver function to test above functions
arrr = [1, 2, 3, 4, 5, 6, 7]
leftRotattre(arrr, 2)  # Rotate array by 2
printrArray(arrr)
