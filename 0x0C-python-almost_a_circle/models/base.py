#!/usr/bin/python3
class Base:
        __nb_objects = 0
        
        def __init__(self, id=None) -> None:
                if id is not None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = Base.__dir____nb_objects