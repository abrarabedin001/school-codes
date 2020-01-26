import random
Arr=[]
for r in range (10):
    a = str(chr(random.randint(65, 90)))
    b = str(chr(random.randint(65, 90)))
    c = str(random.randint(65, 90))
    d = str(random.randint(65, 90))
    e = str(random.randint(65, 90))
    f = str(random.randint(65, 90))
    Arr.append(a+b+c+d+e+f)

print(Arr)