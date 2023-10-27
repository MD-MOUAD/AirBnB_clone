#!/usr/bin/python3
""" Console module for AirBnB """
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        "Quit command to exit the program\n"
        return True

    def do_EOF(self, arg):
        "EOF (ctrl + d) command to exit the program\n"
        print()
        return True

    def emptyline(self):
        "an empty line + ENTER should not execute anything"
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
