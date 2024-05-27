import math
file1, file2 = input(), input()
file1 = open(file1, "r")
file2 = open(file2,"r")

xc, yc = file1.readline().split()
xc, yc = float(xc), float(yc)
radius = int(file1.readline())

points = file2.readlines()
file1.close()
file2.close()

for p in points:
    x, y = float(p.split()[0]), float(p.split()[1])
    res = math.sqrt((x - xc)**2 + (y - yc)**2)
    if res > radius:
        print(2)
    elif res < radius:
        print(1)
    else:
        print(0)
    
