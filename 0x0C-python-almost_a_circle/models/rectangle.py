#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
        def __init__(self, width, height, x=0, y=0, id=None):
                super().__init__(id)
                self.set_height(height)
                self.set_width(width)
                self.set_x(x)
                self.set_y(y)
        
        def set_width(self, width):
                if isinstance(width, int):
                        raise TypeError("width must be an integer")
                elif width <= 0:
                        raise ValueError("width must be > 0")
                else:
                        self.__width = width
        
        def set_height(self, height):
                if isinstance(height, int):
                        raise TypeError("height must be an integer")
                elif height <= 0:
                        raise ValueError("height must be > 0")
                else:
                        self.__height = height
                
        def set_x(self, x):
                if isinstance(x, int):
                        raise TypeError("x must be an integer")
                elif x < 0:
                        raise ValueError("x must be > 0")
                else:
                        self.__x = x
        
        def set_y(self, y):
                if isinstance(y, int):
                        raise TypeError("y must be an integer")
                elif y < 0:
                        raise ValueError("y must be > 0")
                else:
                        self.__y = y