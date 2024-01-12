import random
import sys
import os

game_over = False

class Player:
    weapon_list = []
    current_enemy_list = []
    score = 0
    def __init__(self, name, health, max_health, strength):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.current_weapon = self.weapon_list[0]
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
            self.current_weapon = self.weapon_list[num]
            print('You equipped {name}'.format(name = self.weapon_list[num].name))
    
    def attack(self, enemy):
        self.current_weapon.harm(enemy)
    
    def victory(self):
        print('you\'ve survived the encounter')
        self.score += 1
        self.current_enemy.pop()
        self.encounter()

    def encounter(self):
        self.current_enemy_list.append(enemy_list[random.randint(0, 1)])
        print('A {name} has appeared.'.format(name = self.current_enemy[0].name))
        print('What do you choose to do?')
        fight()
    


class Enemy:
    def __init__(self, name, health, max_health, strength, identity):
        self.name = name
        self.health = health
        self.max_health = max_health
        self.strength = strength
        self.id = identity
        self.is_dead = False
        self.is_current_enemy = False

    def enemy_death(self):
        if self.health <= 0:
            self.health = 0
            self.is_dead = True
            print('{name} has fallen into a slumber'.format(name = self.name))
            self.is_current_enemy = False
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
        if self.name == a.name:
            player.health -= 1
            print('You cut yourself on the sharp edge for 1hp.')
            if player.health <= 0:
                player.death()
            
            
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
a = Weapon('A shard of glass', 2, 1, 7)
b = Weapon('A rusty knife', 3, 1, 2)
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


player = Player(input_name, 1, 1, 5)
player.switch_weapon(1)
    #Game start
def encounter():
    player.encounter()
def fight():
    print('{name}({hp}/{max_hp}hp) is fighting {enemy_name} ({enemy_hp}/{enemy_max_hp}hp).'.format(name = player.name, hp = player.health, max_hp = player.max_health, enemy_name = player.current_enemy_list[0].name, enemy_hp = player.current_enemy_list[0].health, enemy_max_hp = player.current_enemy_list[0].max_health))
    action = input('-->')
    if action == 'attack' or action == 'a':
        player.attack(player.current_enemy[0])

def gameover():
    if player.is_dead = True:
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

