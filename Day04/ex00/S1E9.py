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
        if self.is_alive == True:
            self.is_alive = False


def main():
    """
    Ex00
    """
    args = sys.argv
    if len(args) == 1:
        try:
            print("nima")
        except Exception as e:
            print(e)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()