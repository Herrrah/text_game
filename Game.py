import random
import math
import sys
import os
############################################################### PLAYER

class Player:
    weapon_list = []
    buff_list = []
    current_enemy_list = []
    num = 0
    score = 0
    encounter_scaling = 0
    def __init__(self, name, health, max_health, strength):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.current_weapon = self.weapon_list[self.num]
        self.is_dead = False
        self.current_enemy = self.current_enemy_list

    def __repr__(self):
        description = '{name}, {hp}/{max_hp}HP, {strength} Str, currently using {current}, out of {list}'.format(name = self.name, hp = self.health, max_hp = self.max_health, strength = self.strength, current = self.current_weapon, list = self.weapon_list)
        return description

    def death(self):
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
            print('You perished in your dreams')
            print('You slayed {score} fiends.'.format(score = self.score))
            input('...')
            gameover()
    
    def lose_health(self, amount):
        damage_amount = amount - self.current_weapon.defense
        if damage_amount < 0:
            inverse_block = self.current_weapon.defense - amount
            damage_amount = 1
        self.health -= damage_amount
        if self.health <= 0:
            print('\nYou were fatally struck for {amount}dmg.'.format(amount = amount))
            input('...')
            self.death()
        else:
            if self.current_weapon.defense > 0:
                if damage_amount == 1:
                    print(('\nYou were hit for {amount}dmg, but blocked {block}.'.format(amount = amount, block = inverse_block)))
                else:
                    print(('\nYou were hit for {amount}dmg, but blocked {block}.'.format(amount = amount, block = self.current_weapon.defense)))
            else:
                print('\nYou were hit for {amount}dmg.'.format(amount = amount))
            
            input('...')

    
    def switch_weapon(self, num):
        if num <= len(self.weapon_list) and num >= 0:
            self.num = num
            self.current_weapon = self.weapon_list[self.num]
    
    def attack(self, enemy):
        self.current_weapon.harm(enemy)
    
    def victory(self):
        os.system('cls')
        old_hp = self.health
        heal = math.ceil(self.max_health / 3)
        self.health += heal
        if self.health == self.max_health:
            return
        elif self.health > self.max_health:
            self.health = self.max_health
            print('You survived.\n\nYou feel refreshed\n+{hp}HP'.format(hp = self.max_health - old_hp))
            
        else:
            print('You survived.\n\nYou feel refreshed\n+{hp}HP'.format(hp = heal))
            
        
        self.score += 1
        input('...')

    def encounter(self):
        self.encounter_scaling += 1
        new_enemy = enemy_list[random.randint(0, len(enemy_list) - 1)]
        new_enemy_instance = Enemy(new_enemy.name, new_enemy.health + player.encounter_scaling, new_enemy.max_health + player.encounter_scaling, new_enemy.strength + player.encounter_scaling, new_enemy.speed + player.encounter_scaling)

        self.current_enemy_list.append(new_enemy_instance)
        self.current_enemy_list[-1].health = self.current_enemy_list[-1].max_health
        print('\nA {name} has appeared.'.format(name = self.current_enemy_list[-1].name))
        print('What do you choose to do?')
        input('...')
        fight()

    def boss_encounter(self):
        self.encounter_scaling += 1
        new_boss = boss_list[0]
        new_boss_instance = Boss(new_boss.name, new_boss.health + player.encounter_scaling, new_boss.max_health + player.encounter_scaling, new_boss.strength + player.encounter_scaling, new_boss.speed + player.encounter_scaling)
        self.current_enemy_list.append(new_boss_instance)
        print('\nOut of the void appears a dangerous being')
        print('You feel frightened')
        input('...')
        boss_fight()
    

################################################################## ENEMIES

class Enemy:
    strength_buff_counter = 0
    speed_buff_counter = 0
    def __init__(self, name, health, maximum, strength, speed):
        self.name = name
        self.health = health
        self.max_health = maximum 
        self.strength = strength
        self.speed = speed 
        self.is_dead = False
        self.is_poisoned = False

    def enemy_attack(self):
        player.lose_health(self.strength)
    
    def enemy_special(self):
        if self.name == malformed_despair.name:
            self.strength_buff_counter += 1
            self.strength += 1
            print('\n{name} wails.'.format(name = self.name))
        elif self.name == wretched_eye.name:
            heal_amount = 2
            if self.health == self.max_health:
                self.enemy_attack()
            else:
                if self.health < 10:
                    self.health += heal_amount
                    if self.health > self.max_health:
                        self.health = self.max_health       
                else:
                    heal_amount = self.health / 2
                    self.health +=  heal_amount

                print('\n{name} stared into your soul and felt satiated,\n+{hp}HP'.format(name = self.name, hp = heal_amount))
        elif self.name == rift_walker.name:
            if self.speed >= 9:
                print('{name} tries to gain more speed but can\'t'.format(name = self.name))
            else:
                self.speed_buff_counter += 1
                self.speed+=1
                print('{name} is gaining momentum'.format(name = self.name))
        input('...')
            

    
    def poison_lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print('{name} fell ill.'.format(name = self.name, amount = amount))
            input('...')
            self.enemy_death()
        else:
            print('You poisoned {name} for {amount}dmg.'.format(name = self.name, amount = amount))
            input('...')
            
    def enemy_death(self):
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
            self.strength -= self.strength_buff_counter
            self.strength_buff_counter = 0
            self.speed -= self.speed_buff_counter
            self.speed_buff_counter = 0
            print('{name} has fallen into a slumber'.format(name = self.name))
            

    def enemy_lose_health(self, amount):
        dodge_chance = random.randint(2, 10)
        if self.speed > dodge_chance:
            print('{name} evaded your attack.'.format(name = self.name))
        else:
            self.health -= amount
            if self.health <= 0:
                print('You struck the creature for {amount}dmg.'.format(amount = amount))
                self.enemy_death()
            else:
                print('{name} has been injured for {amount}dmg.'.format(name = self.name, amount = amount))
        
################################################################### WEAPONS

class Weapon:
    def __init__(self, name, power, speed, crit, defense, scaling = 0, poison = False):
        self.name = name
        self.power = power
        self.speed = speed
        self.crit = crit
        self.defense = defense
        self.poison = poison
        self.scaling = scaling

    def __repr__(self):
        description = '{name}'.format(name = self.name)
        return description

    def harm(self, enemy):
        random_number_crit = random.randint(1, 10)
        random_number_crit2 = random.randint(1, 10)
        double_hit_chance = random.randint(0, 4)
        if self.name == b.name:
            player.health -= 1 + (self.power + player.strength - 2)
            print('You cut yourself on the sharp edge for {amount}dmg.'.format(amount = 1 + (self.power + player.strength- 2)))
            if player.health <= 0:
                player.death()
                gameover()
        elif self.name == c.name:
            print('The Iron Maiden was cast, and you have lost it')
            enemy.enemy_lose_health(self.power + player.strength)
            player.weapon_list.remove(c)
            player.current_weapon = player.weapon_list[-1]

        elif self.speed >= 2:
            if double_hit_chance >= 1:
                print('Your swiftness enabled you to strike {amount} more time(s)!'.format(amount = double_hit_chance))
                for i in range(1, (double_hit_chance + 1)):
                    if enemy.is_dead == False:
                        enemy.enemy_lose_health((self.power + player.strength - 1))


        if self.poison == True:
            enemy.is_poisoned = True
                    
        if self.crit >= random_number_crit:
            if enemy.is_dead == False:
                if self.name == b.name:
                    print('EXTRA Critical!')
                    enemy.enemy_lose_health((self.power + player.strength) * 3)
                else:
                    print('Critial!')
                    enemy.enemy_lose_health((self.power + player.strength) * 2)
        elif self.crit <= random_number_crit:
            if enemy.is_dead == False:
                enemy.enemy_lose_health(self.power + player.strength) 

###################################################################### BOSS
class Boss:
    strength_buff_counter = 0
    speed_buff_counter = 0
    def __init__(self, name, health, max_health, strength, speed):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.speed = speed
        self.is_dead = False
        self.is_poisoned = False

        def poison_lose_health(self, amount):
            self.health -= amount
            if self.health <= 0:
                print('{name} fell ill.'.format(name = self.name, amount = amount))
                input('...')
                self.enemy_death()
            else:
                print('You poisoned {name} for {amount}dmg.'.format(name = self.name, amount = amount))
                input('...')
            
    def enemy_death(self):
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
            self.strength -= self.strength_buff_counter
            self.strength_buff_counter = 0
            self.speed -= self.speed_buff_counter
            self.speed_buff_counter = 0
            print('{name} has disappeared into the void'.format(name = self.name))
            

    def enemy_lose_health(self, amount):
        dodge_chance = random.randint(1, 10)
        if self.speed > dodge_chance:
            print('{name} evaded your attack.'.format(name = self.name))
        else:
            self.health -= amount
            if self.health <= 0:
                print('You fatally struck {name} for {amount}dmg.'.format(name = self.name, amount = amount))
                self.enemy_death()
            else:
                print('{name} has been injured for {amount}dmg.'.format(name = self.name, amount = amount))
    
    def enemy_attack(self):
        player.lose_health(self.strength)

    def boss_heal(self):
        self.health = self.max_health
        print('{name} performs a ritual.\nFully healed.'.format(name = self.name))
    
    def boss_buff(self):
        self.strength_buff_counter += 3
        self.strength += 3
        print('{name}\'s blood is pumping\nPower increased.')
    
###################################################################### Buffs
class Buff:
    def __init__(self, name):
        self.name = name
###################################################################### Enemy Objects    


wretched_eye = Enemy('Wretched Eye', 7, 7, 2, 1)
malformed_despair = Enemy('Malformed Despair', 5, 5, 4, 0)
rift_walker = Enemy('Rift Walker', 3, 3, 2, 5)
enemy_list = [wretched_eye, malformed_despair, rift_walker]

wahke = Boss('Wahke Raiker', 300, 300, 0, 0)
boss_list = [wahke]
###################################################################### Weapon Objects

a = Weapon('Rusty Knife', 2, 2, 1, 0)
b = Weapon('Shard of Glass', 2, 1, 9, 0)
c = Weapon('Iron Maiden', 20, 1, 1, 0)
d = Weapon('Sword of the fallen', 4, 1, 3, 3)
e = Weapon('Putrid Crowbar', 3, 1, 0, 1, True)
f = Weapon('Onyx Barrier', 4, 1, 0, 7)


weapons_list = [a, b, c, d, e, f]
###################################################################### Buff Objects

health = Buff('Frigid Hearth')
rage = Buff('Unbridled emotinon')
buffs_list = [health, rage]


 #Input -
def start():
    os.system('cls')
    print('''\n███    ██ ██  ██████  ██   ██ ████████ ███    ███  █████  ██████  ███████     ███████ ██    ██ ███████ ██      
████   ██ ██ ██       ██   ██    ██    ████  ████ ██   ██ ██   ██ ██          ██      ██    ██ ██      ██      
██ ██  ██ ██ ██   ███ ███████    ██    ██ ████ ██ ███████ ██████  █████       █████   ██    ██ █████   ██      
██  ██ ██ ██ ██    ██ ██   ██    ██    ██  ██  ██ ██   ██ ██   ██ ██          ██      ██    ██ ██      ██      
██   ████ ██  ██████  ██   ██    ██    ██      ██ ██   ██ ██   ██ ███████     ██       ██████  ███████ ███████ ''')   
    print('\nYou\'re stuck in an infinite maze, you can\'t remember for how long, but you can feel that you\'ve been here before...\n')
    input('\nPress any button to continue')

#Character Creator + Intro -
def main():
    os.system('cls')
    global player

    input_name = input('\nWhat was your name again...\n-->')
    os.system('cls')
    print('\nYes of course... your name is {name}.\nThere\'s |A Rusty Knife| and |A Shard of Glass| in front of you'.format(name = input_name))
    print('\n | 1 | 2 | ')
    weapon_selection = input('\nPick. one. up.\n-->')
    while weapon_selection < '1' or weapon_selection > '2':
        weapon_selection = input('\nYou have to pick either one\n-->')
    
    if weapon_selection == '1':
        Player.weapon_list.append(a)
    elif weapon_selection == '2':
         Player.weapon_list.append(b)
    player = Player(input_name, 10, 10, 0)
    print('You picked up {name}, how foolish.'.format(name = player.weapon_list[0].name))
    input('...')
    #Game start
def encounter():
    if player.score == 10:
        player.boss_encounter()
    else:
        player.encounter()

def fight():
    while not player.is_dead:
        os.system('cls')
        if player.current_enemy_list[-1].is_dead:
            player.current_enemy_list[-1].is_poisoned = False
            player.victory()
            loot_drop()
            encounter()
            break
        print('                          | {score} fiends slain | '.format(score = player.score))
        print('\n       | {name} ({hp}/{max_hp}hp) is fighting {enemy_name} ({enemy_hp}/{enemy_max_hp}hp) | '.format(name = player.name, hp = player.health, max_hp = player.max_health, enemy_name = player.current_enemy_list[-1].name, enemy_hp = player.current_enemy_list[-1].health, enemy_max_hp = player.current_enemy_list[-1].max_health))
        print('\n| a:attack | s:swap weapon | e:check equipped weapon | i:enemy info | ')
        action = input('-->')
        if action == 'attack' or action == 'a':
            player.attack(player.current_enemy_list[-1])
            input('...')
        elif action == 'swap' or action == 's':
            while len(player.weapon_list) == 1:
                print('\nYou only have one weapon.')
                input('...')
                fight()
            else:
                print('\n | Press a number | ')
                weapon_swap = input('\nwhich weapon would you like to swap to?\n{weapons}\n-->'.format(weapons = player.weapon_list))
                while weapon_swap == '' or weapon_swap.isdigit() == False or int(weapon_swap) > len(player.weapon_list) or int(weapon_swap) < 1:
                    weapon_swap = input('\nYou can\'t trick the Dream\n-->')
                if player.weapon_list[int(weapon_swap) - 1] == player.current_weapon:
                    print('\nYou\'re already holding that weapon.')
                elif int(weapon_swap) <= len(player.weapon_list) or int(weapon_swap) > 0:
                    player.switch_weapon(int(weapon_swap) - 1)
                    print('\nYou swapped to {name}'.format(name = player.current_weapon))
                input('...')
                fight()
        elif action == 'equip' or action == 'e':
            print('\nYou\'re holding | {name} | {power} Power | {speed} Speed | {crit} Crit | {defense} Defense | '.format(name = player.current_weapon.name, power = player.current_weapon.power + player.strength, speed = player.current_weapon.speed, crit = player.current_weapon.crit, defense = player.current_weapon.defense))
            if player.current_weapon == a:
                print('\nA rusty knife you picked up, it feels light')
            if player.current_weapon == b:
                print('\nHigh chance of critical but injures self')
            if player.current_weapon.name == c.name:
                print('\nExtremely powerful but single use')
            if player.current_weapon == d:
                print('\nA beautiful sword, it was made for vanquishing evil.')
            if player.current_weapon == e:
                print('\nIt reeks of dung. Afflicts enemies with poison.')
            if player.current_weapon == f:
                print('\nIt\'s shining, you feel protected.')
            input('...')
            fight()
        elif action == 'info' or action == 'i':
            print('\n{name} | {strength} Strength |'.format(name = player.current_enemy_list[-1].name, strength = player.current_enemy_list[-1].strength))
            if player.current_enemy_list[-1] == wretched_eye:
                print('\nA curius Eye, it delights in seeing your suffering.\nChance to heal itself.')
            elif player.current_enemy_list[-1] == malformed_despair:
                print('\nTheir face is contorted in a perpetual expression of pain\nChance to power up')
            elif player.current_enemy_list[-1] == rift_walker:
                print('\nThis creature is barely visible, who knows for how long they\'ve been here\nChance to evade')
            input('...')
            fight()
        else:
            fight()
        if player.is_dead:
            gameover()
        else:
            if not player.current_enemy_list[-1].is_dead:
                if player.current_enemy_list[-1].is_poisoned:
                    player.current_enemy_list[-1].poison_lose_health(int(e.power))
                if not player.current_enemy_list[-1].is_dead:
                    enemy_action = random.randint(0, 5)
                    if enemy_action <= 2:
                        player.current_enemy_list[-1].enemy_attack()
                    else:
                        player.current_enemy_list[-1].enemy_special()
                    fight()
                else:
                    player.current_enemy_list[-1].is_poisoned = False
                    player.victory()
                    loot_drop()
                    encounter() 
            else:
                player.current_enemy_list[-1].is_poisoned = False
                player.victory()
                loot_drop()
                encounter()
    if player.is_dead:
        gameover()
        


def loot_drop():
    if player.score % 2 == 0:
        buff_pickup()
    else:
        global possible_loot
        possible_loot = []

        numbers = list(range(0, len(weapons_list)))
        random.shuffle(numbers)
        possible_loot.append(weapons_list[numbers[0]])
        possible_loot.append(weapons_list[numbers[1]])
        possible_loot.append(weapons_list[numbers[2]])
        loot_pickup()

def loot_pickup():
    if player.score % 2 == 0:
        loot_drop()
    else:
        os.system('cls')
        selection = input('Out of the void appears a Glimmer\n\n | {loot1} | {loot2} | {loot3} | \n\nChoose wisely...\n-->'.format(loot1 = possible_loot[0], loot2 = possible_loot[1], loot3 = possible_loot[2]))
        while selection.isdigit() == False or int(selection) <= 0 or int(selection) > len(possible_loot):
            selection = input('\nChoose one.\n-->')
        if possible_loot[int(selection) - 1] in player.weapon_list:
            print('\nYour {name} grew stronger.'.format(name = possible_loot[int(selection) - 1].name))
            input('...')
            possible_loot[int(selection) - 1].scaling += 1
            if possible_loot[int(selection) -1] == c:
                possible_loot[int(selection) - 1].power += 2
            if possible_loot[int(selection) -1] == f:
                possible_loot[int(selection) -1].defense += 1

            possible_loot[int(selection) - 1].power += 1

        else:
            player.weapon_list.append(possible_loot[int(selection) - 1])
            print('\nYou picked up {name}.'.format(name = player.weapon_list[-1].name))
            input('...')

def buff_pickup():
    os.system('cls')
    selection = input('Well done for surviving this long.\nAn exceedingly bright shine emanates.\n\n | {buff1} | {buff2} |\n\nPick at your heart\'s content\n-->'.format(buff1 = buffs_list[0].name, buff2 = buffs_list[1].name))
    while selection.isdigit() == False or int(selection) <= 0 or int(selection) > len(buffs_list):
        selection = input('\nChoose one.\n-->')
    if selection == '1':
        player.buff_list.append(buffs_list[0])
        print('A wash of tranquility washes over you\n+10 Max HP\nFully healed')
        player.max_health += 10
        player.health = player.max_health
    elif selection == '2':
        player.buff_list.append(buffs_list[1])
        print('Your heart drums with intensity.\n+1 Strength to all weapons\nFully healed')
        player.strength += 1
        player.health = player.max_health
    input('...')

def boss_fight():

    while not player.is_dead:
            os.system('cls')
            if player.current_enemy_list[-1].is_dead:
                player.current_enemy_list[-1].is_poisoned = False
                player.victory()
                loot_drop()
                encounter()
                break
            print('                          | {score} fiends slain | '.format(score = player.score))
            print('\n       | {name} ({hp}/{max_hp}hp) is fighting {enemy_name} ({enemy_hp}/{enemy_max_hp}hp) | '.format(name = player.name, hp = player.health, max_hp = player.max_health, enemy_name = player.current_enemy_list[-1].name, enemy_hp = player.current_enemy_list[-1].health, enemy_max_hp = player.current_enemy_list[-1].max_health))
            print('\n| a:attack | s:swap weapon | e:check equipped weapon | i:enemy info | ')
            action = input('-->')
            if action == 'attack' or action == 'a':
                player.attack(player.current_enemy_list[-1])
                input('...')
            elif action == 'swap' or action == 's':
                while len(player.weapon_list) == 1:
                    print('\nYou only have one weapon.')
                    input('...')
                    boss_fight()
                else:
                    print('\n | Press a number | ')
                    weapon_swap = input('\nwhich weapon would you like to swap to?\n{weapons}\n-->'.format(weapons = player.weapon_list))
                    while weapon_swap == '' or weapon_swap.isdigit() == False or int(weapon_swap) > len(player.weapon_list) or int(weapon_swap) < 1:
                        weapon_swap = input('\nYou can\'t trick the Dream\n-->')
                    if player.weapon_list[int(weapon_swap) - 1] == player.current_weapon:
                        print('\nYou\'re already holding that weapon.')
                    elif int(weapon_swap) <= len(player.weapon_list) or int(weapon_swap) > 0:
                        player.switch_weapon(int(weapon_swap) - 1)
                        print('\nYou swapped to {name}'.format(name = player.current_weapon))
                    input('...')
                    boss_fight()
            elif action == 'equip' or action == 'e':
                print('\nYou\'re holding | {name} | {power} Power | {speed} Speed | {crit} Crit | {defense} Defense | '.format(name = player.current_weapon.name, power = player.current_weapon.power + player.strength, speed = player.current_weapon.speed, crit = player.current_weapon.crit, defense = player.current_weapon.defense))
                if player.current_weapon == a:
                    print('\nA rusty knife you picked up, it feels light')
                if player.current_weapon == b:
                    print('\nHigh chance of critical but injures self')
                if player.current_weapon.name == c.name:
                    print('\nExtremely powerful but single use')
                if player.current_weapon == d:
                    print('\nA beautiful sword, it was made for vanquishing evil.')
                if player.current_weapon == e:
                    print('\nIt reeks of dung. Afflicts enemies with poison.')
                if player.current_weapon == f:
                    print('\nIt\'s shining, you feel protected.')
                input('...')
                boss_fight()
            elif action == 'info' or action == 'i':
                print('\n{name} | {strength} Strength |'.format(name = player.current_enemy_list[-1].name, strength = player.current_enemy_list[-1].strength))
                if player.current_enemy_list[-1] == wahke:
                    print('An enigma, said to only exist within the psyche of souls.\nUnpredictable, fearsome\n\nYou best be careful.')   
                input('...')
                boss_fight()
            else:
                boss_fight()
            if player.is_dead:
                gameover()
            else:
                if not player.current_enemy_list[-1].is_dead:
                    if player.current_enemy_list[-1].is_poisoned:
                        player.current_enemy_list[-1].poison_lose_health(int(e.power))
                    if not player.current_enemy_list[-1].is_dead:
                        enemy_action = random.randint(0, 20)
                        if enemy_action <= 5:
                            player.current_enemy_list[-1].enemy_attack()
                        elif enemy_action > 5 and enemy_action < 10:
                            player.current_enemy_list[-1].boss_heal()
                        elif enemy_action >= 10 and enemy_action <= 12:
                            player.current_enemy_list[-1].boss_buff()
                        elif enemy_action > 12 and enemy_action <= 20:
                            print('The enemy laughs at your pitiful state')
                        input('...')
                        boss_fight()
                    else:
                        player.current_enemy_list[-1].is_poisoned = False
                        player.victory()
                        loot_drop()
                        encounter() 
                else:
                    player.current_enemy_list[-1].is_poisoned = False
                    player.victory()
                    loot_drop()
                    encounter()
    if player.is_dead:
        gameover()





def gameover():
    os.system('cls')
    option = input('\n[Restart]\n-->')
    while option.isdigit() == False or int(option) != 1:
        option = input('\n-->')
    if int(option) == 1:
        player.score = 0
        for enemy in player.current_enemy_list:
            enemy.health -= player.encounter_scaling
            enemy.max_health -= player.encounter_scaling
            enemy.strength -= player.encounter_scaling
            enemy.is_poisoned = False
        for weapon in player.weapon_list:
            if weapon == c:
                weapon.power -= weapon.scaling * 3
            else:
                weapon.power -= weapon.scaling 
        player.current_enemy_list = []
        player.encounter_scaling = 0
        player.weapon_list.clear()
        player.is_dead = False
        player.current_enemy.pop()
        start()
        main()
        encounter()

        
start()
main()
encounter()
