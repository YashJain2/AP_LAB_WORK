class Square:
    def  __init__(self,height="0",width="0"):
        self.height=height
        self.width=width

    @property
    def height(self):
        print("retrieving the height :")
        return self.__height

    @height.setter
    def height(self,value):
        if value.isdigit():
            self.__height=value
        else:
            print("Please only enter numbers for height")

    @property
    def width(self):
        print("retrieving the width :")
        return self.__width

    @width.setter
    def width(self,value):
        if value.isdigit():
            self.__width=value
        else:
            print("Please only enter numbers for width")

    def area(self):
        return (int(self.__width) * int(self.__height))


def main():
    square=Square()
    height=input("Enter Height :")
    width=input("Enter Width :")
    square.height=height
    square.width=width
    print("Height :" ,square.height)
    print("Width :", square.width)
    print("The area is :", square.area())

main()
