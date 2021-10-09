def swap(p):
    size = len(p)

    temp = p[0]
    p[0] = p[size-1]
    p[size-1] = temp
    return p
    
p = [1,4,54,67,34]
print(swap(p))
