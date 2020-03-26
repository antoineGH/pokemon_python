# IMPORT

from Pokemon_class import Pokemon
from Trainer_class import Trainer

# INSTANTIATION

squirtle = Pokemon("Squirtle", 5, "Water", True)
charmander = Pokemon("Charmander", 5, "Fire", True)
bulbasaur = Pokemon("Bulbasaur", 5, "Grass", True)

squirtle.attack(charmander)
squirtle.attack(charmander)
squirtle.attack(charmander)
squirtle.attack(charmander)
squirtle.attack(charmander)
squirtle.attack(charmander)
squirtle.attack(charmander)

squirtle.level_up()
squirtle.level_up()
squirtle.level_up()
squirtle.level_up()
squirtle.level_up()
squirtle.level_up()
squirtle.level_up()

squirtle.restore_health(50)
squirtle.restore_health(1000)