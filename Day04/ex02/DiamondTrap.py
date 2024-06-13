from S1E7 import Baratheon, Lannister
import sys


class King(Baratheon, Lannister):
    def get_eyes(self):
        """sets the eyes based on the second parent and returns it"""
        temp_char = Lannister.create_lannister("temp")
        self.eyes = temp_char.eyes
        del temp_char
        return self.eyes

    def get_hairs(self):
        """sets the hair based on the second parent and returns it"""
        temp_char = Lannister.create_lannister("temp")
        self.hair = temp_char.hair
        del temp_char
        return self.hair

    def set_eyes(self, new_eyes):
        """sets the eyes based on the new input"""
        self.eyes = new_eyes

    def set_hairs(self, new_hairs):
        """sets the hair based on the new input"""
        self.hair = new_hairs


def main():
    """
    Ex02
    """
    args = sys.argv
    if len(args) == 2:
        try:
            king = King(args[1])
            print(f"{king} is created")
        except Exception as e:
            print(e)
    else:
        try:
            raise AssertionError("The wrong number of arguments is provided")
        except AssertionError as e:
            print(e)


if __name__ == "__main__":
    main()
