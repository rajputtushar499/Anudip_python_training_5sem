import geometry

print("Select a figure:")
print("1. Circle")
print("2. Rectangle")
print("3. Square")

figure_choice = int(input("Enter your choice (1-3): "))

if figure_choice == 1:

    radius = float(input("Enter the radius of the circle: "))

    while True:
        print("1. Area")
        print("2. Perimeter")
        print("3. Exit")

        operation = int(input("Enter your choice: "))

        if operation == 1:
            print("Area of Circle:", geometry.area_circle(radius))

        elif operation == 2:
            print("Perimeter of Circle:", geometry.perimeter_circle(radius))

        elif operation == 3:
            break

elif figure_choice == 2:

    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    while True:
        print("\n1. Area")
        print("2. Perimeter")
        print("3. Exit")

        operation = int(input("Enter your choice: "))

        if operation == 1:
            print("Area of Rectangle:",geometry.area_rectangle(length, width))

        elif operation == 2:
            print("Perimeter of Rectangle:",geometry.perimeter_rectangle(length, width))

        elif operation == 3:
            break

elif figure_choice == 3:

    side = float(input("Enter the side of the square: "))

    while True:
        print("\n1. Area")
        print("2. Perimeter")
        print("3. Exit")

        operation = int(input("Enter your choice: "))

        if operation == 1:
            print("Area of Square:", geometry.area_square(side))

        elif operation == 2:
            print("Perimeter of Square:",geometry.perimeter_square(side))

        elif operation == 3:
            break

else:
    print("Invalid choice Please select a valid figure.")
