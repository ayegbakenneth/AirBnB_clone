#!/usr/bin/python3
""" A program that contains entry point of the console"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This is the HolbertonBnB class of the command line interpreter.

        A custom prompt: (str): The command prompt.
    """
    
    prompt = "(hbnb) "
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, arg):
        """The command to exit the program."""
        return True
    
    def help_quit(self, arg):
        """This action is provided by default by cmd."""
        print("A command to exit the program")

    def do_EOF(self, arg):
        """ An End of file which signals to exit the program."""
        print()
        return True

    def do_create(self, arg):
        """ Creates a new instance of BaseModel, saves it (to the JSON file) 
        and prints the id.
        """
        parsed_arguments = split(arg)
        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_object = BaseModel()
            new_object.save()
            print(new_object.id)

    def do_show(self, arg):
        """
        Display the string representation of a class instance of a given id.
        """
        parsed_arguments = split(arg)
        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(parsed_arguments) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = "{}.{}".format(parsed_arguments[0], parsed_arguments[1])
            if key in instances:
                print(instances[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        and save the change into the JSON file.
        """
        parsed_arguments = split(arg)
        
        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(parsed_arguments) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = "{}.{}".format(parsed_arguments[0], parsed_arguments[1])
            if key in instances:

                del instances[key]
                storage.save()
            else:
               print("** no instance found **")

    def do_all(self, arg):
        """ Prints all string representation of all instances 
        based or not on the class name."""
        instances = storage.all()
        parsed_arguments = split(arg)
        if len(parsed_arguments) == 0:
            for key, value in instances.items():
                 print(str(value))
        elif parsed_arguments[0] not in self.__classes:
             print("** class doesn't exist **")
        else:
            for key, value in instances.items():
                if key.split(',')[0] == parsed_arguments[0]:
                    print(str(value))

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding 
        or updating attribute save the change into the JSON file."""
        parsed_arguments = split(arg)

        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.__classes:
            print("** class doesn't exist **")
        if len(parsed_arguments) < 2:
            print("** instance id missing **")
        else:
            instances = storage.all()
            key = "{}.{}".format(parsed_arguments[0], parsed_arguments[1])
            if key not in instances:
                print("** no instance found **")
            elif len(parsed_arguments) < 3:
                print("** attribute name missing **")
            elif len(parsed_arguments) < 4:
                print("** value missing **")
            else:
                obj = instances[key]
                attr_name = parsed_arguments[2]
                attr_value = parsed_arguments[3]
                try:
                    attr_value = (eval(attr_value))
                except Exception:
                    pass
                setattr(obj, attr_name, attr_value)
                obj.save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
