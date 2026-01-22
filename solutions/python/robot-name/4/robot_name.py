from string import ascii_uppercase, digits
import random as r


class Robot:
    used = set()

    def __init__(self):
        self.name = self.robo_name()

        while self.name in Robot.used:
            self.name = self.robo_name()
        
        Robot.used.add(self.name)
        
    def robo_name(self):
        letters = ''.join(r.choices(ascii_uppercase, k = 2))
        numbers = ''.join(r.choices(digits, k = 3))

        return (name := letters + numbers)
    
    def reset(self):
        reset = self.robo_name()

        while reset in Robot.used:
            reset = self.robo_name()

        Robot.used.discard(self.name)

        self.name = reset
        
        Robot.used.add(reset)
