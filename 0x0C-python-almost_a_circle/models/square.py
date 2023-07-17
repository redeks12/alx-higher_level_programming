#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):
        def __init__(self, size ,x=0, y=0, id=None):
                '''A representation of the base of our OOP hierarchy.'''
                super().__init__(size,size,x, y, id)
           
        @property
        def size(self):
                '''A representation of the base of our OOP hierarchy.'''
                '''size of this rectangle.'''
                return self.width

        @size.setter
        def size(self, value):
                '''A representation of the base of our OOP hierarchy.'''
                self.int_check("width", value,False)
                self.width = value
                self.height = value
        
        def __str__(self) -> str:
                '''A representation of the base of our OOP hierarchy.'''
                return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)
        
        def __update(self,id=None,size=None,x=None,y=None):
                '''A representation of the base of our OOP hierarchy.'''
                if id is not None:
                        self.id = id
                if size is not None:
                        self.width = size
                        self.height = size
                if x is not None:
                        self.x = x
                if y is not None:
                        self.y = y
        def update(self, *args, **kwargs):
                '''A representation of the base of our OOP hierarchy.'''
                if args:
                        self.__update(*args)
                else:
                        self.__update(**kwargs)
                        
        def to_dictionary(self):
                '''A representation of the base of our OOP hierarchy.'''
                return {"id": self.id, "x": self.x, "y": self.y,"size": self.size}
