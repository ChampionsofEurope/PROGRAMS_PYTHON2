
def arge(arr, n):

    max = arr[0]


    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max


arr = [14, 84, 98, 90, 56]
n = len(arr)
ans = arge(arr, n)
print("Largest in given array is", ans)
