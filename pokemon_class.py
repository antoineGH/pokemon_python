class Pokemon:

    uid = 0
    evolution = {"Squirtle": ["Squirtle", "Wartortle", "Blastoise"], 
             "Charmander": ["Charmander", "Charmeleon", "Charizard"],
             "Bulbasaur": ["Bulbasaur", "Ivysaur", "Venusaur"], 
             "Pidgey": ["Pidgey", "Pidgeotto", "Pidgeot"]}
    
    def __init__(self, name, level, type, alive, owner = None):     
        self.name = name
        self.level = level
        self.type = type
        self.alive = alive
        self.owner = owner
        self.family = self.name
        self.experience = 0
        self.health = 50
        self.max_health = self.health * self.level
        self.id = name + str(self.uid)
        Pokemon.uid += 1

    def __repr__(self):
        return ("{} - Type {} - {} ({}/{}HPs) - Level {} ({}/100XP)".format(self.name, self.type, self.get_status(), self.health, self.max_health, self.level, self.experience))

    def get_status(self):
        if self.alive:
            return "Alive"
        else:
            return "Dead"

    def is_alive(self):
        return self.alive == True

    def is_target_alive(self, target):
        return target.alive == True

    def knock_out(self):
        if self.is_alive():
            self.alive = False
            self.health = 0
            print("> Oh no! {} is {}".format(self.name, self.get_status()))
        else:
            print("> {} is already dead.".format(self.name))
    
    def revive(self):
        print("--- Reviving {} ---".format(self.name))
        if self.alive == False:
            self.alive = True
            self.health = self.max_health // 2
            print("> Reviving {} with {}HPs.\n".format(self.name, self.health))
        else:
            print("> {} is already alive.\n".format(self.name))

    def lose_health(self, lost_hp):
        if self.is_alive():
            self.health -= lost_hp
            if self.health > 0:
                print("> {} Losts {} HPs. Now has {}/{}HPs.\n".format(self.name, lost_hp, self.health, self.max_health))
            elif self.health <= 0:
                self.knock_out()
            else:
                print("> {} is already dead.".format(self.name))

    def restore_health(self, restore_hp):
        if self.is_alive():
            self.health += restore_hp
            if self.health >= self.max_health:
                self.health = self.max_health
            print("> {} heals {} HPs. ({}/{}HPs.)".format(self.name, restore_hp, self.health, self.max_health))
        else:
            print("> Can't heal, {} is dead.".format(self.name))

    def damage_boost(self, target):
        if self.type == "Fire" and target.type == "Water":
            boost = 0.5
            return boost
        elif self.type == "Water" and target.type == "Fire":
            boost = 0.5
            return boost
        elif self.type == "Fire" and target.type == "Grass":
            boost = 2
            return boost
        elif self.type == "Grass" and target.type == "Fire":
            boost = 0.5
            return boost
        elif self.type == "Grass" and target.type == "Water":
            boost = 2
            return boost
        else:
            boost = 1
            return boost

    def set_name(self):
        if self.family in self.evolution.keys():
            if self.level >= 5 and self.level <10:
                self.name = self.evolution[self.family][1]
            elif self.level >= 10:
                self.name = self.evolution[self.family][2]
        else:
            return

    def level_up(self):
        if self.is_alive():
            self.level += 1
            self.max_health = self.level * self.health
            check_name = self.name
            self.set_name()
            if check_name != self.name:
                print("\n--- Hurray! {} has now evolve into a {}! ---".format(check_name, self.name))
            else:
                print("\n--- Level Up ! ---".format(self.name, self.level))
                print("> {} is now on level {}.".format(self.name, self.level))
                print("> {}".format(self))
        else:
            print("> Can't level up, {} is dead.".format(self.name))

    def add_xp(self, xp):
        if self.is_alive:
            self.experience += xp
            if self.experience >= 100:
                self.level_up()
                rest = self.experience - 100
                self.experience = 0 + rest
            return xp
        else:
            print("> Can't xp, {} is dead.".format(self.name))

    def check_xp(self, target):
        if self.level - 4 >= target.level:
            xp = self.add_xp(40)
        elif self.level + 4 >= target.level:
            xp = self.add_xp(100)
        else:
            xp = self.add_xp(70)
        print("> {} earned {}XP.".format(self.name, xp))
        if xp:
            return xp
        else:
            return
        
    def attack(self, target):
        print("--- {} attacks {} ---".format(self.name, target.name))
        if self.is_alive():
            if self.is_target_alive(target):
                damage = self.damage_boost(target) * self.level * 3
                print("> {} attacks {} and deals {} Damages (Boost x{})".format(self.name, target.name, damage, self.damage_boost(target)))
                target.lose_health(damage)
                if not self.is_target_alive(target):
                    self.check_xp(target)
            else:
                print("> Can't attack target, {} is dead.".format(target.name))
        else:
            print("> Can't attack, {} is dead.".format(self.name))
