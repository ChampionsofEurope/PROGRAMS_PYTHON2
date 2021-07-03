/3.7.21

s = 0

t = 7037279

while t>0:
    d = t%10
    s = s*10+d
    t = t//10
    print(s)
