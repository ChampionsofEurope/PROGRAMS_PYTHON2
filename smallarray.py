
arry = [0, 9, 7, 1, -3]


minny = arry[0]

# Loop through the array
for i in range(0, len(arry)):
    # Compare elements of array with min
    if (arry[i] < minny):
        minny = arry[i]

print("Smallest element present in given array: " + str(minny))
