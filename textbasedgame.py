#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:01:03 2018

@author: stem
"""
import random
player_hp = 60
enemy_hp = random.randint(30, 80)
def enemy_atk(php):
    miss_or_hit = random.randint(1, 3)
    if miss_or_hit == 1:
        print("Enemy missed")
    else:
        enemy_dmg = random.randint(3, 8)
        php = php - enemy_dmg
        print ("Enemy dealt", enemy_dmg, "damage!")
    return php
    
def player_atk(ehp):
    roll = random.randint(1, 6)
    if roll < 3:
        print("You missed!")
    elif roll < 6:
        dmg = random.randint(1, 7)
        ehp = ehp - dmg
        print("You dealt", dmg, "damage!")
    else:
        dmg = 10
        ehp = ehp - dmg
        print("You dealt", dmg, "damage!")
    return ehp

def player_heal(health):
    roll = random.randint(1, 6)
    if roll == 1:
        print("Your heal failed!")
    elif roll < 6:
        heal = random.randint(1, 6)
        print("You healed", heal, "hp!")
        health = heal + health
    else:
        heal = 8
        print("You healed 10 hp!!")
        health = heal + health
    return health
def fight(php, ehp):
    while php > 0 and ehp > 0:
        print(php)
        print(ehp)
        a = input("Press 1 for Attack,Press 2 for heal." )
        a = float(a)
        php = enemy_atk(php)
        if a == 1 and php > 0:
            ehp = player_atk(ehp)
        elif a == 2 and php > 0:
            php = player_heal(php)
        else:
            break
    return php
player_hp = fight(player_hp, enemy_hp)
if player_hp <= 0:
    print("GAME OVER!!!")
elif enemy_hp <= 0:
    print("YOU WIN!!!")
        


            
            
