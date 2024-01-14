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
        self.health -= amount
        if self.health <= 0:
            print('\nYou were fatally struck for {amount}dmg.'.format(amount = amount))
            input('...')
            self.death()
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
        self.current_enemy_list.append(enemy_list[random.randint(0, (len(enemy_list) - 1))])
        self.current_enemy_list[-1].is_dead = False
        self.current_enemy_list[-1].health = self.current_enemy_list[-1].max_health
        self.current_enemy_list[-1].is_poisoned = False
        self.current_enemy_list[-1].health += self.encounter_scaling
        self.current_enemy_list[-1].max_health += self.encounter_scaling
        self.current_enemy_list[-1].strength += self.encounter_scaling
        print('\nA {name} has appeared.'.format(name = self.current_enemy_list[-1].name))
        print('What do you choose to do?')
        input('...')
        fight()
    

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
        if player.current_enemy_list[-1] == enemy_list[1]:
            self.strength_buff_counter += 1
            self.strength += 1
            print('\n{name} wails.'.format(name = self.name))
        elif player.current_enemy_list[-1] == enemy_list[0]:
            self.health += 2
            if self.health > self.max_health:
                self.health = self.max_health
                self.enemy_attack()
            else:
                print('\n{name} stared into your soul and felt satiated,\n+{hp}HP'.format(name = self.name, hp = 2))
        elif player.current_enemy_list[-1] == enemy_list[2]:
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
        dodge_chance = random.randint(1, 10)
        if self.speed >= dodge_chance:
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
    def __init__(self, name, power, speed, crit, poison = False):
        self.name = name
        self.power = power
        self.speed = speed
        self.crit = crit
        self.poison = poison

    def __repr__(self):
        description = '{name}'.format(name = self.name)
        return description

    def harm(self, enemy):
        random_number_crit = random.randint(1, 10)
        random_number_crit2 = random.randint(1, 10)
        double_hit_chance = random.randint(0, 4)
        random_bleed_amount = random.randint(1, 2)
        if self.name == b.name:
            player.health -= random_bleed_amount + (self.power + player.strength- 2)
            print('You cut yourself on the sharp edge for {amount}dmg.'.format(amount = random_bleed_amount + (self.power + player.strength- 2)))
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
                    enemy.enemy_lose_health(self.power * 2 + player.strength + 2)
                else:
                    print('Critial!')
                    enemy.enemy_lose_health(self.power * 2 + player.strength)
        elif self.crit <= random_number_crit:
            if enemy.is_dead == False:
                enemy.enemy_lose_health(self.power + player.strength) 
            
###################################################################### Buffs
class Buff:
    def __init__(self, name):
        self.name = name
###################################################################### Enemy Objects    

#Enemies -

wretched_eye = Enemy('Wretched Eye', 7, 7, 2, 1)
malformed_despair = Enemy('Malformed Despair', 5, 5, 4, 0)
rift_walker = Enemy('Rift Walker', 3, 3, 2, 5)
enemy_list = [wretched_eye, malformed_despair, rift_walker]

####################################################################### Weapon Objects

a = Weapon('Rusty Knife', 2, 2, 1)
b = Weapon('Shard of Glass', 2, 1, 8)
c = Weapon('Iron Maiden', 10, 1, 1)
d = Weapon('Flaming Sword', 3, 1, 2)
e = Weapon('Putrid Crowbar', 2, 1, 0, True)


weapons_list = [a, b, c, d, e]
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
    player.encounter()

def fight():
    os.system('cls')
    if player.current_enemy_list[-1].is_dead == False:
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
        print('\nYou\'re holding | {name} | {power} Power | {speed} Speed | {crit} Crit'.format(name = player.current_weapon.name, power = player.current_weapon.power + player.strength, speed = player.current_weapon.speed, crit = player.current_weapon.crit))
        if player.current_weapon == a:
            print('\nA rusty knife you picked up, it feels light')
        if player.current_weapon == b:
            print('\nHigh chance of critical but injures self')
        if player.current_weapon.name == c.name:
            print('\nExtremely powerful but single use')
        if player.current_weapon == d:
            print('\nA beautiful sword, somehow it\'s lit on fire')
        if player.current_weapon == e:
            print('\nIt reeks of dung. Poisons the Enemy')
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
    if player.is_dead == True:
            gameover()
    
    else:
        if player.current_enemy_list[-1].is_dead == False:
            if player.current_enemy_list[-1].is_poisoned == True:
                player.current_enemy_list[-1].poison_lose_health(int(e.power))
            if player.current_enemy_list[-1].is_dead == False:
                enemy_action = random.randint(0,5)
                if enemy_action <= 2:
                    player.current_enemy_list[-1].enemy_attack()
                elif enemy_action == 2 or enemy_action <= 4:
                    player.current_enemy_list[-1].enemy_special()
                elif enemy_action == 5:
                    print('\nThe {name} is staring at you.'.format(name = player.current_enemy_list[-1].name))
                    input('...')
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

def loot_drop():
    if player.score % 4 == 0:
        buff_pickup()
    else:
        global possible_loot
        possible_loot = []

        random_number1 = random.randint(0, len(weapons_list))
        while True:
            random_number2 = random.randint(0, len(weapons_list))
            if random_number2 != random_number1:
                break

        possible_loot.append(weapons_list[random_number1 - 1])
        possible_loot.append(weapons_list[random_number2 - 1])
        loot_pickup()

def loot_pickup():
    if player.score % 4 == 0:
        loot_drop()
    else:
        os.system('cls')
        selection = input('Out of the void appears a Glimmer\n\n | {loot1} | {loot2} | \n\nChoose wisely...\n-->'.format(loot1 = possible_loot[0], loot2 = possible_loot[1]))
        while selection.isdigit() == False or int(selection) <= 0 or int(selection) > len(possible_loot):
            selection = input('\nChoose one.\n-->')
        if possible_loot[int(selection) - 1] in player.weapon_list:
            print('\nYour {name} grew stronger.'.format(name = possible_loot[int(selection) - 1].name))
            input('...')
            if possible_loot[int(selection) -1] == c:
                possible_loot[int(selection) - 1].power += 3

            else: 
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
        print('A wash of tranquility washes over you\n+8 Max HP\nFully healed')
        player.max_health += 8
        player.health = player.max_health
    elif selection == '2':
        player.buff_list.append(buffs_list[1])
        print('Your heart drums with intensity.\n+2 Strength to all weapons\nFully healed')
        player.strength += 2
        player.health = player.max_health
    input('...')


def gameover():
    os.system('cls')
    option = input('\n[Restart]\n-->')
    while option.isdigit() == False or int(option) != 1:
        option = input('\n-->')
    if int(option) == 1:
        player.score = 0
        player.current_enemy_list[-1].health -= player.encounter_scaling
        player.current_enemy_list[-1].max_health -= player.encounter_scaling
        player.current_enemy_list[-1].strength -= player.encounter_scaling
        player.current_enemy_list[-1].is_poisoned = False
        player.current_enemy_list = []
        player.weapon_list.clear()
        player.is_dead = False
        player.current_enemy.pop()
        start()
        main()
        encounter()

        
start()
main()
encounter()
