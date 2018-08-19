from random import randint

class Die():
    """Makes a die and the possibility to roll. """
    def __init__(self,sides=6):
        """Makes a die, with input for how many sides it has. """
        self.sides = sides

    def roll(self, times=1):
        """A function which rolls the die. When the function is called, so
        can one define how many times one can roll the die."""
        for i in range(times):
            x = randint(1,self.sides)
            print("Roll " + str(i+1) + " of " + str(times) + " is " + str(x))


print("A six die, rolling!")
six_die = Die(6)
six_die.roll(10)

print("A ten die, rolling!")
ten_die = Die(10)
ten_die.roll(10)

print("A twenty die, rolling!")
twenty_die = Die(20)
twenty_die.roll(10)
