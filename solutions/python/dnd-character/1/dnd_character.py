import random as r



def modifier(value):
    return (value - 10) // 2

class Character:
    def __init__(self):
        (self.strength, self.constitution, self.dexterity, self.intelligence, self.wisdom, self.charisma) = self.ability_list()

        self.hitpoints = 10 + modifier(self.constitution)
        
        
    def ability_list(self):
        stats = tuple(
                    tuple(
                        inner[:i] + inner[i+1:]
                        for inner in (tuple(sorted(r.randrange(1, 7) for _ in range(4))) for _ in range(6))
                    for i in (inner.index(min(inner)),)
                        )
                    )

        strength, constitution, dexterity, intelligence, wisdom, charisma = sum(stats[0]), sum(stats[1]), sum(stats[2]), sum(stats[3]), sum(stats[4]), sum(stats[5])

        return (strength, constitution, dexterity, intelligence, wisdom, charisma)

    def ability(self):
        return r.choice(self.ability_list())

        
    
    
        

    

    

        
        

