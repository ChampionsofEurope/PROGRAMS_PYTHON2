arr2 = [1, 2, 5, 4, 5, 9, 8, 7, 7, 4, 3, 2, 1]

print("Duplicate elements in given array:")

for i in range(0, len(arr2)):
    for j in range(i + 1, len(arr2)):
        if (arr2[i] == arr2[j]):
            print(arr2[j])
