from abc import ABC, abstractmethod
import sys


class Character(ABC):
    """Character (abstract class)"""
    def __init__(self, first_name, is_alive=True):
        """Character has a first name and is alive or not(by default: alive)"""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Class inherited from Character class"""
    def die(self):
        """changes is_alive attribute to False is alive"""
        if self.is_alive:
            self.is_alive = False


def main():
    """
    Ex00
    """
    args = sys.argv
    if len(args) == 3 or len(args) == 2:
        try:
            if len(args) == 3:
                stark = Stark(sys.args[1], sys.args[2])
            else:
                stark = Stark(sys.args[1])
            print(f"{stark} is created")
        except Exception as e:
            print(e)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
