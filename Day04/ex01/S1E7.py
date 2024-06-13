from S1E9 import Character
import sys


class Baratheon(Character):
    """Baratheon class"""
    def __new__(self, first_name, is_alive=True):
        """creates a lannister without going through the Character class"""
        instance = object.__new__(self)
        instance.first_name = first_name
        instance.is_alive = is_alive
        return instance

    def __init__(self, first_name, is_alive=True):
        """Character has a first name and is alive or not(by default: alive)"""
        super().__init__(first_name, is_alive)
        self.eyes = "blue"
        self.hair = "ligth"

    def die(self):
        """changes is_alive attribute to False is alive"""
        if self.is_alive:
            self.is_alive = False

    def __repr__(self):
        """technical string representation"""
        return f"Lannister Family {self.first_name}"

    def __str__(self):
        """human-readable string representation"""
        return f"Lannister Family {self.first_name}"


class Lannister(Character):
    """Lannister class"""
    def __new__(self, first_name, is_alive=True):
        """creates a lannister without going through the Character class"""
        instance = object.__new__(self)
        instance.first_name = first_name
        instance.is_alive = is_alive
        return instance

    def __init__(self, first_name, is_alive=True):
        """Character has a first name and is alive or not(by default: alive)"""
        super().__init__(first_name, is_alive)
        self.eyes = "blue"
        self.hair = "ligth"

    def die(self):
        """changes is_alive attribute to False is alive"""
        if self.is_alive:
            self.is_alive = False

    def __repr__(self):
        """technical string representation"""
        return f"Lannister Family {self.first_name}"

    def __str__(self):
        """human-readable string representation"""
        return f"Lannister Family {self.first_name}"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """creates a lannister without going through the Character class"""
        return cls(first_name, is_alive)


def main():
    """
    Ex01
    """
    args = sys.argv
    if len(args) == 3 or len(args) == 5:
        try:
            if len(args) == 3:
                baratheon = Baratheon(sys.args[1])
                lannister = Lannister(sys.args[2])
            else:
                baratheon = Baratheon(sys.args[1], sys.args[2])
                lannister = Lannister(sys.args[3], sys.args[4])
            print(f"{baratheon} and {lannister} are created")
        except Exception as e:
            print(e)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
