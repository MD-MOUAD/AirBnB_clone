#!/usr/bin/python3
""" Console module for AirBnB """
import cmd
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """"Class for the console of AirBnB"""

    prompt = "(hbnb) "
    _all_classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """EOF (ctrl + d) command to exit the program
        """
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER should not execute anything
        """
        pass

    def method_error(self, name, arg):
        """Handler for method's error
        return 0 if no error found otherwise 1
        """
        args = arg.split()

        if len(args) < 1 and name != "all":
            print("** class name missing **")
            return 1

        classes = HBNBCommand._all_classes
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
            return 1

        if len(args) < 2 and name not in ["create", "all"]:
            print("** instance id missing **")
            return 1

        if name not in ["create", "all"]:
            instance_key = args[0] + '.' + args[1]
            if instance_key not in storage.all():
                print("** no instance found **")
                return 1

        if name == "update":
            if len(args) < 3:
                print("** attribute name missing **")
                return 1
            if len(args) < 4:
                print("** value missing **")
                return 1

        return 0

    def do_create(self, arg):
        """Creates a new instance:
Usage: create <class name>
        """
        if not self.method_error("create", arg):
            classes = HBNBCommand._all_classes
            name = arg.split()[0]
            if name in classes:
                # create new instance of the class and save it
                new = classes[name]()
                new.save()
                print(new.id)

    def do_show(self, arg):
        """Prints the string representation of an instance:
Usage: show <class name> <instance id>
        """
        if self.method_error("show", arg) == 0:
            args = arg.split()
            instance_key = args[0] + '.' + args[1]
            obj = storage.all()[instance_key]
            print(obj)

    def do_destroy(self, arg):
        """Deletes an instance
Usage: destroy <instance id>
        """
        if self.method_error("destroy", arg) == 0:
            args = arg.split()
            instance_key = args[0] + '.' + args[1]
            del storage.all()[instance_key]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
Usage: all
Usage: all <class name>
        """
        if not self.method_error("all", arg):
            args = arg.split()
            list_obj = []
            if len(args) > 0:    # Usage: all <class name>
                name = args[0]
                for key, value in storage.all().items():
                    if name in key:
                        list_obj.append(str(value))
            else:                # Usage: all
                for obj in storage.all().values():
                    list_obj.append(str(obj))
            print(list_obj)

    def do_update(self, arg):
        """Updates an instance by adding or updating attribute:
Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not self.method_error("update", arg):
            args = arg.split()
            instance_key = args[0] + '.' + args[1]
            obj = storage.all()[instance_key]
            if args[3][0] == '"' and args[3][-1] == '"':
                args[3] = args[3][1:-1]
            if args[3][0] == "'" and args[3][-1] == "'":
                args[3] = args[3][1:-1]
            if hasattr(obj, args[2]):
                data_type = type(getattr(obj, args[2]))
                try:
                    args[3] = data_type(args[3])
                    setattr(obj, args[2], args[3])
                except ValueError:
                    print(f"can't update {args[2]}: invalid type")
            else:
                setattr(obj, args[2], args[3])
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
