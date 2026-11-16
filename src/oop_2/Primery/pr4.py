class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    def height(self):
        return self.__height
    def area(self):
        return self.__width * self.__height
    def set_width(self, width):
        self.__width = width
    def set_height(self, height):
        self.__height = height

rect = Rectangle(10,20)
print(rect.width(), rect.height())
print(rect._Rectangle__width)
rect._Rectangle__width=20
