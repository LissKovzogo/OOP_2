class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height
    @property
    def width(self):
        return self.__width
    @width.setter
    def width(self, w):
        if w > 0:
            self.__width = w
        else:
            raise ValueError("width must be positive")
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, h):
        if h > 0:
            self.__height = h
        else: raise ValueError("height must be positive")
    def area(self):
        return self.__width * self.__height



rect = Rectangle(10,20)
rect.width = 100
rect.height = 200
print(rect.width(), rect.height())
