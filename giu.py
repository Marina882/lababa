a = int(input("введите коэффициент а:"))
b = int(input("введите коэффициент b:"))
c = int(input("введите коэффициент c:"))
D = ((b*b-b) - (4*a*c*a))

if D >= 0:
    x1 = ((-b + D ** (1/2)) / (2*a))
    x2 = ((-b - D ** (1/2)) / (2*a))
    print(x1, x2)
else:
    print("Корней нет")
