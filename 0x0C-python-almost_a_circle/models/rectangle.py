#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
        def __init__(self, width, height, x=0, y=0, id=None):
                '''Constructor'''
                super().__init__(id)
                self.height = height
                self.width = width
                self.y = y
                self.x= x

        @property
        def width(self):
                '''Get the width'''
                return self.__width
        
        @width.setter
        def width(self, width):
                '''Set the width'''
                self.valid_int(width, "width")
                if width <= 0:
                        raise ValueError("width must be > 0")
                self.__width = width
        @property
        def height(self):
                '''Get the height'''
                return self.__height
        
        @height.setter
        def height(self, height):
                '''Set the height'''
                self.valid_int(height,"height")
                if height <= 0:
                        raise ValueError("height must be > 0")
                self.__height = height
        @property
        def x(self):
                '''get x'''
                return self.__x
        @x.setter
        def x(self, x):
                '''set x'''
                self.valid_int(x, "x")
                if x < 0:
                        raise ValueError("x must be >= 0")
                self.__x = x
        @property
        def y(self):
                '''get y'''
                return self.__y
        @y.setter
        def y(self, y):
                '''set y'''
                self.valid_int(y, "y")
                if y < 0:
                        raise ValueError("y must be >= 0")
                self.__y = y
                
        def valid_int(self, typ, name):
                '''validate int type'''
                if type(typ) != int():
                        raise TypeError("{} must be an integer".format(name))