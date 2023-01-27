import math
a = 2
b = 4
c = 3

disc =  (b**2) - (4*a*c)

if disc < 0:
    print("no tiene solución")
else:
    x = (-b + math.sqrt(disc)) /(2*a)
    y = (-b - math.sqrt(disc)) /(2*a)
    print(x, y)