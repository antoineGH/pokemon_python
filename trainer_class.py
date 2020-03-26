class Trainer:
    def __init__(self, name, nb_potions):
        self.name = name
        self.nb_potions = nb_potions
        self.pokelist = []
        self.active = None

    def __repr__(self):
        return ("> {} - Pokemons:\n{}".format(self.name, self.show_pokelist()))

    def show_pokelist(self):
        if len(self.pokelist) > 0:
            print("\n--- Display {}'s Pokedex ---".format(self.name))
            for pokemon in self.pokelist:
                print(">> {} - Type {} - {} ({}/{}HPs) - Level {} ({}/100XP) - {}".format(pokemon.name, pokemon.type, pokemon.get_status(), pokemon.health, pokemon.max_health, pokemon.level, pokemon.experience, pokemon.is_active()))
        else:
            print("> {} has no Pokemon ... Yet !".format(self.name))

    def add_pokelist(self, pokemon):
        if len(self.pokelist) < 6:
            self.pokelist.append(pokemon)
            pokemon.owner = self
            print("> Adding {} to {}'s Pokedex.".format(pokemon.name, self.name))
            if len(self.pokelist) == 1:
                self.active = self.pokelist[0]
                pokemon.active = True
                print("> {} Define as a default active Pokemon.".format(self.pokelist[0].name))
            return
        else:
            user_input = input("> {}'s Pokedex Full, Remove Pokemon? y/n: ".format(self.name, self.show_pokelist()))
            if user_input.lower() == "y":
                self.remove_pokelist()
                self.add_pokelist(pokemon)
            else:
                return

    def remove_pokelist(self):
        if len(self.pokelist) > 0:
            print("\n--- Remove from Pokedex ---")
            list_index = [i for i in range(len(self.pokelist))]
            for index in list_index:
                print("> Press {} to remove {} - Type {} - {} ({}/{}HPs) - Level {} ({}/100XP)".format(index, self.pokelist[index].name, self.pokelist[index].type, self.pokelist[index].get_status(), self.pokelist[index].health, self.pokelist[index].max_health, self.pokelist[index].level, self.pokelist[index].experience))
            user_input = int(input(">> Remove Pokemon Choice: "))
            if user_input in list_index:
                if self.pokelist[user_input].active:
                    self.active = self.pokelist[-1]
                    print("> {} Define as a default active Pokemon.".format(self.pokelist[-1].name))
                self.pokelist[user_input].owner = None
                print("> Removing {} from {}'s Pokedex".format(self.pokelist[user_input].name, self.name))
                self.pokelist.remove(self.pokelist[user_input])
                return
            else:
                user_continue = input("> Choice not in the list, Try again? y/n: ")
                if user_continue.lower() == "y":
                    self.remove_pokelist()
                else:
                    return

    def set_active(self):
        list_index = [i for i in range(len(self.pokelist))]
        print("\n--- Set Active Pokemon ---")
        for index in list_index:
            print("> Press {} to active {} - Type {} - {} ({}/{}HPs) - Level {} ({}/100XP) - {}".format(index, self.pokelist[index].name, self.pokelist[index].type, self.pokelist[index].get_status(), self.pokelist[index].health, self.pokelist[index].max_health, self.pokelist[index].level, self.pokelist[index].experience, self.pokelist[index].is_active()))
        user_input = int(input(">> Active Pokemon Choice: "))
        if user_input in list_index:
            if self.pokelist[user_input].is_alive():
                self.active = self.pokelist[user_input]
                print("> Define {} as active Pokemon".format(self.pokelist[user_input].name))
                return
            else:
                print("> Please choose an alive Pokemon")
                self.set_active()
        else:
            print("> Choice not in the list")
            self.set_active()

    def use_potion(self):
        if self.nb_potions > 0:
            self.nb_potions -= 1
            self.active.restore_health(50)

    def attack_trainer(self, target_trainer):
        print("\n--- Trainer {} use {} to attack Trainer {} defends with {} ---".format(self.name, self.active.name, target_trainer.name, target_trainer.active.name))
        if self.active != None:
            if target_trainer.active != None:
                if self.active.is_alive():
                    if target_trainer.active.is_alive():
                        self.active.attack(target_trainer.active)
                    else:
                        print("> Target {} is Dead, Pick Alive Pokemon to defend !")
                        target.set_active()
                        self.attack_trainer(target_trainer)
                        return
                else:
                    print("> Your {} is Dead, Pick Alive Pokemon to attack !")
                    self.set_active()
                    self.attack_trainer(target_trainer)
                    return
            else:
                print("> Trainer target {} should select an active Pokemon!".format(target.name))
                target.set_active()
                self.attack_trainer(self, target_trainer)
                return
        else:
            print("> Trainer {} an active Pokemon!".format(self.name))
            self.set_active()
            self.attack_trainer(self, target_trainer)
            return