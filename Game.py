import random
import sys
import os

game_over = False

class Player:
    weapon_list = []
    current_enemy_list = []
    num = 0
    score = 0
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
            game_over = True
    
    def lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.death()
        else:
            print('you\'ve been hit for {amount}dmg!'.format(amount = amount))

    
    def switch_weapon(self, num):
        if num <= len(self.weapon_list) and num >= 0:
            self.num = num
            self.current_weapon = self.weapon_list[self.num]
            print('You equipped {name}'.format(name = self.current_weapon.name))
    
    def attack(self, enemy):
        self.current_weapon.harm(enemy)
    
    def victory(self):
        print('you\'ve survived the encounter')
        self.score += 1

    def encounter(self):
        self.current_enemy_list.append(enemy_list[random.randint(0, 1)])
        self.current_enemy_list[0].is_dead = False
        self.current_enemy_list[0].health = self.current_enemy_list[0].max_health
        print('A {name} has appeared.'.format(name = self.current_enemy[0].name))
        print('What do you choose to do?')
        fight()
    


class Enemy:
    def __init__(self, name, health, maximum, strength, identity):
        self.name = name
        self.health = health
        self.max_health = maximum
        self.strength = strength
        self.id = identity
        self.is_dead = False

    def enemy_death(self):
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
            print('{name} has fallen into a slumber'.format(name = self.name))
            player.victory()

    def enemy_lose_health(self, amount):
        self.health -= amount
        if self.health <= 0:
            print('You struck the creature for {amount}dmg.'.format(amount = amount))
            self.enemy_death()
        else:
            print('{name} has been injured for {amount}dmg.'.format(name = self.name, amount = amount))
        

    def enemy_attack(self):
        Player.lose_health(self.strength)
        

class Weapon:

    def __init__(self, name, power, speed, crit, poison = 0):
        self.name = name
        self.power = power
        self.speed = speed
        self.crit = crit
        self.poison = 0

    def __repr__(self):
        description = '{name}'.format(name = self.name)
        return description

    def harm(self, enemy):
        if self.name == b.name:
            player.health -= 1
            print('You cut yourself on the sharp edge for 1hp.')
            if player.health <= 0:
                player.death()
        if self.name == c.name:
            print('The Iron Maiden was cast, and you have lost it')
            player.weapon_list.remove(c)
        if self.crit > random.randint(0, 10):
            print('Critial!')
            enemy.enemy_lose_health(self.power * 2)
            
        else:
            enemy.enemy_lose_health(self.power)
    
 #Input -       
print('You\'re stuck in an infinite maze, you can\'t remember for how long, but you can feel that you\'ve been here before...')
input('Press any button to continue')
input_name = input('What was your name again...')
#Enemies -
wretched_eye = Enemy('Wretched eye', 4, 4, 3, 1)
malformed_despair = Enemy('Malformed head', 4, 4, 5, 2)
enemy_list = [wretched_eye, malformed_despair]
#Weapons -
a = Weapon('A rusty knife', 3, 1, 2)
b = Weapon('A shard of glass', 2, 1, 7)
c = Weapon('Iron Maiden', 10, 1, 1)
p = Weapon('Fist', 1, 1, 1)
#Character Creator + Intro -
def main():
    global player
Player.weapon_list.append(p)
print('Yes of course... your name is {name}.\nThere\'s a rusty knife and a shard of glass in front of you'.format(name = input_name))

weapon_selection = input('Pick. one. up. press 1 or 2\n-->')
while weapon_selection < '1' or weapon_selection > '2':
    weapon_selection = input('You have to pick either one\n-->')
    
if weapon_selection == '1':
    Player.weapon_list.append(a)
elif weapon_selection == '2':
     Player.weapon_list.append(b)


player = Player(input_name, 10, 10, 5)
player.switch_weapon(1)
    #Game start
def encounter():
    player.encounter()

def fight():
    print('{name}({hp}/{max_hp}hp) is fighting {enemy_name} ({enemy_hp}/{enemy_max_hp}hp).'.format(name = player.name, hp = player.health, max_hp = player.max_health, enemy_name = player.current_enemy_list[0].name, enemy_hp = player.current_enemy_list[0].health, enemy_max_hp = player.current_enemy_list[0].max_health))
    action = input('-->')
    if action == 'attack' or action == 'a':
        player.attack(player.current_enemy[0])
    if action == 'swap' or action == 's':
        weapon_swap = input('which weapon would you like to swap to?\n{weapons}\n{numbers}\n-->'.format(weapons = player.weapon_list, numbers = range(1, len(player.weapon_list), 1)))
        while int(weapon_swap) > len(player.weapon_list) or int(weapon_swap) < 1:
            weapon_swap = input('You can\'t trick the Dream\n-->')
        if player.weapon_list[int(weapon_swap) - 1] == player.current_weapon:
            input('You\'re already holding that weapon.\n-->') 
        if int(weapon_swap) <= len(player.weapon_list) or int(weapon_swap) > 0:
            player.switch_weapon(int(weapon_swap) - 1)
    if action == 'equip' or action == 'e':
        print('you\'re holding' + player.current_weapon.name)
    if player.current_enemy[0].is_dead == True:
        player.current_enemy.pop()
        loot_drop()
    else:
        fight()
def loot_drop():
    global possible_items
    possible_items = []
    random_number1 = 1
    random_number2 = random.randint(0, 5)
    random_number3 = random.randint(0, 5)
    if random_number1 == 1:
        possible_items.append(c)
    loot_pickup()
    encounter()

def loot_pickup():
    selection = input('out of the void appears a glimmer\n{loot}\nChoose wisely...\n-->'.format(loot = possible_items))
    while int(selection) <= 0 or int(selection) > len(possible_items):
        selection = input('Choose one.')
    if int(selection) <= len(possible_items) > 0:
        player.weapon_list.append(possible_items[int(selection) - 1])
        print('You picked up {name}.'.format(name = player.weapon_list[-1].name))

def gameover():
    if player.is_dead == True:
        player.score = 0
        player.health = player.max_health
        player.current_enemy_list = []
        weapon_list = []

main()
encounter()
#player.current_enemy[0].enemy_attack()
#player.switch_weapon(1)
#player.attack(player.current_enemy[0])
#player.current_enemy[0].enemy_attack()
#player.switch_weapon(0)
#player.attack(player.current_enemy[0])
#player.attack(player.current_enemy[0])
#player.attack(player.current_enemy[0])
#player.current_enemy[0].enemy_attack()

