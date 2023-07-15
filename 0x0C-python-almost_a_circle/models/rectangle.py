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
                self.__width = width
        
        def set_height(self, height):
                self.__height = height
                
        def set_x(self, x):
                self.__x = x
        
        def set_y(self, y):
                self.__y = y