#!/usr/bin/python3
"""
This module contains the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """ Do nothing on empty line + ENTER."""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
