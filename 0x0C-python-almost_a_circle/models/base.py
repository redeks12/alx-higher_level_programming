#!/usr/bin/python3
import json, csv

class Base:
        __nb_objects = 0
        
        def __init__(self, id=None) -> None:
                if id is not None:
                        self.id = id
                else:
                        Base.__nb_objects += 1
                        self.id = Base.__nb_objects
        @staticmethod           
        def to_json_string(list_dictionaries):
                if not list_dictionaries or list_dictionaries is None:
                        return []
                
                return json.dumps(list_dictionaries)
        
        @classmethod
        def save_to_file(cls, list_objs):
                if list_objs is not None:
                        list_objs = [o.to_dictionary() for o in list_objs]
                with open("{}.json".format(cls.__name__), "w") as file:
                        file.write(cls.to_json_string(list_objs))
        
        @staticmethod
        def from_json_string(json_string):
                if not json_string or json_string is None:
                        return []
                return json.loads(json_string) 
        
        @classmethod
        def create(cls, **dictionary):
                from models.rectangle import Rectangle
                from models.square import Square
                if cls == Square:
                        new_c = Square(1)
                elif cls == Rectangle:
                        new_c = Rectangle(1,2)
                else:
                        new_c = None
                        
                new_c.update(**dictionary)
                return new_c
        
        @classmethod
        def load_from_file(cls):
                from os import path
                file = "{}.json".format(cls.__name__)
                if path.isfile(file):
                        return []
                with open(file , "r") as file:
                      [cls.create(**d) for d in cls.from_json_string(file.read())]
                      
        @classmethod
        def save_to_file_csv(cls, list_objs):
                from models.rectangle import Rectangle
                from models.square import Square
                
                if list_objs is not None:
                        if cls == Square:
                                list_objs = [[o.id, o.size, o.x, o.y] for o in list_objs]
                        if cls == Rectangle:
                                list_objs = [[o.id, o.width, o.height ,o.x, o.y] for o in list_objs]
                                
                with open(f"{cls.__name__}.csv", "w") as file:
                        writ = csv.writer(file)                
                        writ.writerows(list_objs)
        
        @classmethod
        def load_from_file_csv(cls): 
                from models.rectangle import Rectangle
                from models.square import Square      
                main_arr = []         
                with open("{}.csv".format(cls.__name__),'r', newline="", encoding='utf-8') as file:
                        rd = csv.reader(file)
                
                        for row in rd:
                                if not row:
                                        continue
                                row = [int(rw) for rw in row]
                                if cls == Rectangle:
                                        cl = {
                                                'id' : row[0],
                                                'width': row[1],
                                                'height': row[2],
                                                'x': row[3],
                                                'y': row[4],
                                        }
                                
                                if cls == Square:
                                        cl = {
                                                'id' : row[0],
                                                'size': row[1],
                                                'x': row[2],
                                                'y': row[3],                                        
                                        }
                                        
                                main_arr.append(cls.create(**cl))
                return main_arr
        @staticmethod
        def draw(list_rectangles, list_squares):
                '''to draw the line representations of the class'''
                from turtle import Turtle, Screen
                screen = Screen()
                for sqr in list_squares:
                        tim = Turtle()
                        tim.penup()
                        tim.goto(x=sqr.x, y=sqr.y)
                        tim.pendown()
                        for _ in range(4):
                                tim.forward(sqr.width)
                                tim.left(90)
                for rec in list_rectangles:                        
                        tim.penup()
                        tim.goto(x=rec.x, y=rec.y)
                        tim.pendown()
                        for _ in range(2):
                                tim.forward(rec.width)
                                tim.left(90)
                                tim.forward(rec.height)
                                tim.left(90)        
                
                screen.exitonclick()
             








