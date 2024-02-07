#!/usr/bin/python3

import cmd
from datetime import datetime


class BaseModel:
    pass


class User(BaseModel):
    pass


class Place(BaseModel):
    pass


class State(BaseModel):
    pass


class City(BaseModel):
    pass


class Amenity(BaseModel):
    pass


class Review(BaseModel):
    pass


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print(eval(line)().id)

    def do_show(self, line):
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print(eval(line).id)

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print(eval(line).id)

    def do_all(self, line):
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            print(eval(line).id)

    def do_update(self, line):
        if not line:
            print("** class name missing **")
        elif line not in ["BaseModel", "User", "Place", "State", "City", "Amenity", "Review"]:
            print("** class doesn't exist **")
        else:
            prin
