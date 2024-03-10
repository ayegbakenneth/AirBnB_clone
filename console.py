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
        parsed_arguments = shlex.split(arg)
        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            new_object = BaseModel()
            new_object.save()
            print(new_object.id)

    def do_show(self, arg):
        """
        Display the string representation of a class instance of a given id.
        """
        parsed_arguments = shlex.split(arg)
        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(parsed_arguments) == 1:
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
        parsed_arguments = shlex.split(arg)
        
        if len(parsed_arguments) == 0:
            print("** class name missing **")
        elif parsed_arguments[0] not in self.valid_classes:
            print("** class doesn't exist **")
        elif len(parsed_arguments) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            instances = storage.all()
            key = "{}.{}".format(parsed_arguments[0], parsed_arguments[1])
            if key in instances:

                del instances[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects."""
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """Usage: count <class> or <class>.count()
        Retrieve the number of instances of a given class."""
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or
       <class>.update(<id>, <attribute_name>, <attribute_value>) or
       <class>.update(<id>, <dictionary>)
        Update a class instance of a given id by adding or updating
        a given attribute key/value pair or dictionary."""
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
