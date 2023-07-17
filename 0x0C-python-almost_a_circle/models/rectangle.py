#!/usr/bin/python3
from models.base import Base
class Rectangle(Base):
        def __init__(self, width, height, x=0, y=0, id=None):
                '''Constructor.'''
                super().__init__(id)
                self.width = width
                self.height = height
                self.x = x
                self.y = y

        @property
        def width(self):
                '''Width of this rectangle.'''
                return self.__width

        @width.setter
        def width(self, value):
                self.int_check("width", value, False)
                self.__width = value

        @property
        def height(self):
                '''Height of this rectangle.'''
                return self.__height

        @height.setter
        def height(self, value):
                self.int_check("height", value, False)
                self.__height = value

        @property
        def x(self):
                '''x of this rectangle.'''
                return self.__x

        @x.setter
        def x(self, value):
                self.int_check("x", value)
                self.__x = value

        @property
        def y(self):
                '''y of this rectangle.'''
                return self.__y

        @y.setter
        def y(self, value):
                self.int_check("y", value)
                self.__y = value

        def int_check(self, name, value, eq=True):
                '''Method for validating the value.'''
                if type(value) != int:
                    raise TypeError("{} must be an integer".format(name))
                if eq and value < 0:
                    raise ValueError("{} must be >= 0".format(name))
                elif not eq and value <= 0:
                    raise ValueError("{} must be > 0".format(name))
        def area(self):
                return self.height * self.width
        def display(self):
                for _ in range(self.height):
                        for _ in range(self.x):
                                print(" ", end="")
                        for _ in range(self.width):
                                print("#",end="")
                        print()
        def __str__(self) -> str:
               return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)
        
        def __update(self, id=None, width=None, height=None, x=None, y=None): 
                if id is not None:
                        self.id = id
                if width is not None:
                        self.width = width
                if height is not None:
                        self.height = height
                if x is not None:
                        self.x = x
                if y is not None:
                        self.y = y

        def update(self, *args, **kwargs):
                if args:
                        self.__update(*args)
                else:
                        self.__update(**kwargs)
        
        def to_dictionary(self):
                return {"id": self.id, "x": self.x, "y": self.y,"width": self.width, "height": self.height}
                
        
                        
                        
