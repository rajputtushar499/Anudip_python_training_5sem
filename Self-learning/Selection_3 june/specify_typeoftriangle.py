a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides form a triangle")

    if a == b == c:
        print("It is an Equilateral Triangle")
    elif a == b or b == c or a == c:
        print("It is an Isosceles Triangle")
    else:
        print("It is a Scalene Triangle")
else:
    print("The sides do not form a triangle")
