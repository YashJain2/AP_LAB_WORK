import math
def get_area(shape):
    shape=shape.lower()
    if shape =="rectangle":
        rectangle_area()
    elif shape=="circle":
        circle_area()
    else:
        print("Please enter rectangle or circle")

def rectangle_area():
    length=float(input("Enter the length :"))
    width=float(input("Enter the width :"))
    area=length*width
    print("The area of the rectangle is :",area)

def circle_area():
    radius=float(input("Enter the radius :"))
    area=math.pi *(math.pow(rafius,2))
    print("the area of the circle is : {:.2f}".format(area))

def main():
    shape_type=input("Get area of what shape ?")
    get_area(shape_type)

main()
