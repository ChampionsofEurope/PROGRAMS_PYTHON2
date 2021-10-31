
arry = [7890,9870,10078,67890,67891]


biggy = arry[0]

# Loop through the array
for i in range(0, len(arry)):
    if (arry[i] > biggy):
        biggy = arry[i]

print("Largest element present in given array: " + str(biggy))
