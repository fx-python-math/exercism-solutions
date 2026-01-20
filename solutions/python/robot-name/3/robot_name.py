from string import ascii_uppercase, digits
import random as r


class Robot:
    used = set()

    def __init__(self):
        self.name = self.robo_name()
        Robot.used.add(self.name)
        

    def robo_name(self):
        letters = ''.join(r.choices(ascii_uppercase, k = 2))
        numbers = ''.join(r.choices(digits, k = 3))

        name = letters + numbers

        return name
    
    def reset(self):
        reset = self.robo_name()

        while reset in Robot.used:
            reset = self.robo_name()

        Robot.used.discard(self.name)

        new_name = reset

        self.name = new_name

        Robot.used.add(new_name)
