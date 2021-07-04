/4.7.21

j = [6,4,2,8,5,12,4,20]
maxmuin = j[0]
minumin = j[0]

for i in j:
    if i>maxmuin:
        maxmuin = i

for i in j:
    if minumin>i:
        minumin = i

print(maxmuin)
print(minumin)
