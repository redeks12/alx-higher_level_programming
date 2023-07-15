#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
        def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.height = height
                self.width = width
                self.y = y
                self.x= x

        @property
        def width(self):
                return self.__width
        
        @width.setter
        def set_width(self, width):
                self.valid_int(width, "width")
                if width <= 0:
                        raise ValueError("width must be > 0")
                self.__width = width
        @property
        def height(self):
                return self.__height
        
        @height.setter
        def set_height(self, height):
                self.valid_int(height,"height")
                if height <= 0:
                        raise ValueError("height must be > 0")
                self.__height = height
        @property
        def x(self):
                return self.__x
        @x.setter
        def set_x(self, x):
                self.valid_int(x, "x")
                if x < 0:
                        raise ValueError("x must be >= 0")
                self.__x = x
        @property
        def y(self):
                return self.__y
        @y.setter
        def set_y(self, y):
                self.valid_int(y, "y")
                if y < 0:
                        raise ValueError("y must be >= 0")
                self.__y = y
                
        def valid_int(self, typ, name):
                if type(typ) != int():
                        raise TypeError("{} must be an integer".format(name))