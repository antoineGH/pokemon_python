# IMPORT

from pokemon_class import Pokemon
from trainer_class import Trainer

# INSTANTIATION

squirtle = Pokemon("Squirtle", 5, "Water", True)
charmander = Pokemon("Charmander", 5, "Fire", True)
sharmander = Pokemon("Sharmander", 5, "Fire", True)
bulbasaur = Pokemon("Bulbasaur", 5, "Grass", True)
bulbastrur = Pokemon("Bulbastrur", 5, "Grass", True)
bulbretasaur = Pokemon("Bulbretasaur", 5, "Grass", True)
butretrelbasaur = Pokemon("Butretrelbasaur", 5, "Grass", True)

antoine = Trainer("Antoine", 3)
bastien = Trainer("Bastien", 3)

bastien.add_pokelist(squirtle)
antoine.add_pokelist(charmander)
antoine.add_pokelist(sharmander)
antoine.add_pokelist(bulbasaur)
antoine.add_pokelist(bulbastrur)
antoine.add_pokelist(bulbretasaur)
antoine.add_pokelist(butretrelbasaur)


antoine.attack_trainer(bastien)
#squirtle.attack(charmander)
#squirtle.attack(charmander)
#squirtle.attack(charmander)
#squirtle.attack(charmander)
#squirtle.attack(charmander)
#squirtle.attack(charmander)
#squirtle.attack(charmander)

#squirtle.level_up()
#squirtle.level_up()
#squirtle.level_up()
#squirtle.level_up()
#squirtle.level_up()
#squirtle.level_up()
#squirtle.level_up()

#squirtle.restore_health(50)
#squirtle.restore_health(1000)

