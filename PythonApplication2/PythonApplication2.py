import math

print("Enter value of parametr a: (it should be number value)")

try:
    a = int(input())
    if a>0:
        if a>1:
            x = (1-a)/(2*a)
        else:
            x = (a-1)/(2*a)
    else:
        x = math.log(math.sqrt(1 + math.pow(a, 2)), math.e)

    print("X -->",x)
except Exception:
    print("Error")
