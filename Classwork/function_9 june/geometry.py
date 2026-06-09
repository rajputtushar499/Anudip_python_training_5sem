#create a python program which provides a menu to the user to select the 2 dimensional figure(circle, rectangle, square) after selecting the user
# again ask to select a operatiom provide the input of corresponding data for the figure after input of corresponding data again provide a
# menu to select the operation area,perimeter and as per the data provided by user display the result f operation. this task will be repeated
# again and again until user select the option to exit from that figure. 

# Module for Area and Perimeter of 2D Figures

def area_rectangle(length, width):
    return length * width

def perimeter_rectangle(length, width):
    return 2 * (length + width)

def area_square(side):
    return side * side

def perimeter_square(side):
    return 4 * side

def area_circle(radius):
    return 3.14 * radius * radius

def perimeter_circle(radius):
    return 2 * 3.14 * radius
