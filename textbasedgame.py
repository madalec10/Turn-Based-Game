#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:01:03 2018

@author: stem
"""

import random, time
player_hp = 60
maxhp = player_hp
enemy_hp = random.randint(40, 70)
enemy_damage = 5
gold = 300
x = 1
lives = 1
p_total_dmg = 0
t_dmg_counter = 0
dmg_taken = 0
dmg_taken_counter = 0
total_heals = 0
t_h_counter = 0.000000001
turns_taken = 0
SHOPW = {"spear":3, "steel sword":4, "crossbow":5, "flaming crossbow":6, "diamond plated sword":7, "flaming sword":8, "diamond plated flaming sword of awesomeness": 10}
SHOPC = {"hat":15, "boots":15, "gloves":20, "helmet":25, "gauntlets": 25, "greaves":30, "chestplate":35}
SHOPP = {"lesser potion":15, "potion":30, "greater potion":50, "greatest potion":100}
inventoryw = {}
inventoryc = {}
inventoryp = {"lesser potion":15}

def enemy_atk(php):
    global dmg_taken
    global dmg_taken_counter
    miss_or_hit = random.randint(1, 3)
    if miss_or_hit == 1:
        print("Enemy missed")
    else:
        enemy_dmg = random.randint(enemy_damage - 2, enemy_damage + 3)
        php = php - enemy_dmg
        print ("Enemy dealt", enemy_dmg, "damage!")
        dmg_taken += enemy_dmg
        dmg_taken_counter += 1
    return php
    
def player_atk(ehp, x):
    global p_total_dmg
    global t_dmg_counter
    if x == 1:
        roll = random.randint(1, 6)
        if roll < 3:
            print("You missed!")
        elif roll < 6:
            dmg = random.randint(3, 7)
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
        else:
            dmg = 10
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter +=1
    elif x >= 2:
        roll = random.randint(1, 6)
        if roll < 2:
            print("You missed!")
        elif roll < 6:
            dmg = random.randint((x + (x + 1)), (x + (x + 4)))
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
        else:
            dmg = x + (x + 8)
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
    return ehp

def player_heal(health):
    global total_heals
    global t_h_counter
    roll = random.randint(1, 6)
    if health <= maxhp:
        if roll == 1:
            print("Your heal failed!")
        elif roll < 6:
            heal = random.randint(x + 1, x + 5)
            print("You healed", heal, "hp!")
            health = heal + health
            total_heals += heal
            t_h_counter += 1
        else:
            heal = x * 5
            print("You healed", heal, "hp!!")
            health = heal + health
            total_heals += heal
            t_h_counter += 1
    else:
        print("Health is full")
    return health

def player_potion(invp):
    global maxhp
    global player_hp
    global enemy_hp
    print("-" * 20)
    print("POTIONS")
    print("-" * 20)
    for k, v in invp.items():
        print(k, "-", v)
    print("BACK")
    potion = input("What potion do you want to use? ")
    potion.lower
    while potion != "back":
        if potion in invp.keys():
            pick = input("Do you want to use it on yourself or the enemy? (yourself/enemy) ")
            if pick == "yourself":
                r = player_hp + invp[potion]
                if r > maxhp:
                    player_hp = maxhp
                    print("Your health is full.")
                    del invp[potion]
                    break
                elif r < maxhp: 
                    player_hp = player_hp + invp[potion]
                    print("You healed ", invp[potion], "hp!")
                    del invp[potion]
                    break
            elif pick == "enemy":
                enemy_hp = enemy_hp - invp[potion]
                print("You dealt", invp[potion],"damage to the enemy!")
                del invp[potion]
                break
        elif potion == "back":
            break
        else:
            print("That isn't in your inventory.")
            break

def fight(php, ehp):
    global turns_taken
    global total_heals
    global t_h_counter
    global p_total_dmg
    global t_dmg_counter
    global inventoryp
    while php > 0 and ehp > 0:
        turns_taken += 1
        print("Your health is", php)
        print("Enemy's health is", ehp)
        if len(inventoryp) > 0:
            a = input("Press 1 for Attack, Press 2 for heal, Press 3 for potions." )
        else:
            a = input("Press 1 for Attack, Press 2 for heal.")
        if a.isdigit() == True:
            a = float(a)
        php = enemy_atk(php)
        if a == 1 and php > 0:
            ehp = player_atk(ehp, x)
        elif a == 2 and php > 0:
            php = player_heal(php)
        elif a == 3 and php > 0:
            if len(inventoryp) > 0:
                print("-" * 20)
                print("POTIONS")
                print("-" * 20)
                for k, v in inventoryp.items():
                    print(k, "-", v)
                print("BACK")
                potion = input("What potion do you want to use? ")
                potion.lower
                if potion in inventoryp.keys():
                    pick = input("Do you want to use it on yourself or the enemy? (yourself/enemy) ")
                    if pick == ("yourself"):
                        a = php + inventoryp[potion]
                        if a < maxhp:
                            php += inventoryp[potion]
                            print ("You healed", inventoryp[potion],"hp.")
                            total_heals += inventoryp[potion]
                        elif a > maxhp:
                            b = maxhp - php
                            php = maxhp
                            print("You healed back to full life!")
                            total_heals += b
                        t_h_counter += 1
                    elif pick == ("enemy"):
                       ehp -= inventoryp[potion]
                       print ("The enemy took", inventoryp[potion], "damage.")
                       p_total_dmg += inventoryp[potion]
                       t_dmg_counter += 1
                    del inventoryp[potion]
                    turns_taken += 1   
        elif php > 0:
            b = random.randint(1, 4)
            if b == 1:
                print ("You were playing around and did nothing")
            elif b == 2:
                print ("You decided to start dancing")
            elif b == 3:
                print ("You tried to attack, but slipped on the floor")
            else:
                print ("You just stood there and looked the enemy in the eye")
    return php

def stats(p_dmg, dmg_tak, t_heals, p_counter, taken_counter, h_counter, turns):
    if p_counter > 0 and taken_counter > 0 and h_counter > 0:
        avg_dealt = round(p_dmg / p_counter, 2)
        avg_taken = round(dmg_tak / taken_counter, 2)
        avg_heal = round(t_heals / h_counter, 2)
        print("Your average damage dealt was", avg_dealt)
        print("Your average damage taken was", avg_taken)
        print("Your average heal was", avg_heal)
        print("You had", turns,"turns this round")
        
def shop(gld, shpw, shpc, shpp):
    global x
    global gold
    global maxhp
    global inventoryw
    global inventoryc
    global inventoryp
    print("There are weapons in one corner, and clothing in another. There is also plenty of food and little trinkets.") #Add food and trinkets
    print()
    store2 = ""
    while store2 != "leave" or store2 != "no" or store2 != "l":
        print("You have", gold, "gold.")
        store2 = input("Do you want to look at weapons, clothing, potions, or leave? ")
        store2.lower
        if store2 == "weapons":
            print ("-" * 20)
            print ("WEAPONS (if you need to go back, press enter)")
            print ("-" * 20)
            for k, v in shpw.items():
                if k not in inventoryw:
                    print(k, ">", (v ** 3 + 20))
            weapons2 = input("What weapon do you want to buy? ")
            weapons2.lower
            print()
            if weapons2 in shpw.keys():
                gold -= (shpw[weapons2] ** 3 + 20)
                if gold >= 0:
                    if x < shpw[weapons2]:
                        x = shpw[weapons2]
                    inventoryw[weapons2] = shpw[weapons2]
                    print ("You now own a", weapons2)
                else:
                    gold += (shpw[weapons2] ** 3 + 20)
                    print ("You do not have enough gold to buy that.")
            else:
                print("Please tell me exactly what you want.")
            print()
        elif store2 == "clothing":
            print ("-" * 20)
            print ("CLOTHING (if you need to go back, press enter)")
            print ("-" * 20)
            for k, v in shpc.items():
                if k not in inventoryc:
                    print(k, ">", v * 2)
            outfit = input("What peice of clothing do you want to buy? ")
            outfit.lower
            print()
            if outfit in shpc:
                gold -= (shpc[outfit] * 2)
                if gold >= 0:
                    maxhp += (shpc[outfit])
                    inventoryc[outfit] = shpc[outfit]
                    print ("Your max hp is now", maxhp)
                else:
                    gold += (shpc[outfit] * 2)
                    print("You do not have enough gold to but that.")
            else:
                print("That is not available at the moment.")
            print()
        elif store2 == "potions":
            print ("-" * 20)
            print ("POTIONS (if you need to go back, press enter)")
            print ("-" * 20)
            for k, v in shpp.items():
                if k not in inventoryp:
                    print(k, ">", v * 2)
            pt = input("What potion do you want to buy? ")
            pt.lower
            print()
            if pt in shpp:
                gold -= (shpp[pt] * 2)
                if gold >= 0:
                    inventoryp[pt] = shpp[pt]
                    print("You now have a", pt)
                else:
                    gold += (shpp[pt] * 2)
                    print("You do not have enough gold to buy that.")
            else:
                print("That is not available at the moment.")
        elif store2 == "leave" or store2 == "no":
            break

def random_enemy(chance):
    global gold
    global x
    global enemy_damage
    global player_hp
    global lives
    num = random.randint(1,chance)
    player_hp = maxhp
    if num == 3:
        dprint("You have encountered a petty shoplifter.")
    elif num == 4:
        dprint("You have encountered a wild bear!")
    elif num == 5:
        dprint("You have encountered a giant!")
    elif num == 6:
        dprint("You have encountered a wandering chimera!")
    elif num == 7:
        dprint("You have encountered a dragon!")
    elif num > 7:
        dprint("I ran out of enemy names, but you are probably going to die.")
    if num >= 3:
        enemy_hp = random.randint(num * 17, num * 25)
        enemy_damage = random.randint((num * 2), (num * 3))
        player_hp = fight(player_hp, enemy_hp)
        if player_hp <= 0:
            dprint("You have almost been slain, be more careful next time, if there is a next time...")
            lives -= 1
            if lives > 1:
                dprint("You have been slain! GAME OVER!!!")
            else:
                print("Because you died, you have lost 30 gold and now have", gold,"gold.")
        elif player_hp > 0:
            fg = random.randint(num * 6, num * 10)
            gold += fg
            print("You found", fg, "gold from the enemy and now have", gold, "gold.")            

def dprint(string):
    print(string)
    """sleep = 0.05
    for x in string:
        print(x, end = "")
        time.sleep(sleep)"""

shop(gold, SHOPW, SHOPC, SHOPP)
name = input("Please enter your name: ")
while name == "":
    name = input("Please enter your name, I am losing my patience: ")
print()
while lives > 0:
    dprint ("You wake up to a loud crash outside your home. It is quiet for a moment, but then there is another loud bang. You don’t know what is out there, so you grab your sword and some food and venture outside to see what the noise was. A cloaked figure is ransacking your farm and stealing your store for the winter.")
    choice1 = input("Do you wish to investigate? (y/n) ")
    print()
    if choice1 == "y" or choice1 == "yes":
        dprint ("The cloaked figure has attacked you!")
        print()
        player_hp = fight(player_hp, enemy_hp)
        if player_hp <= 0:
            dprint("You were killed by the cloaked figure. GAME OVER!!!")
            lives = 0
        elif player_hp > 0:
            print()
            dprint("With the cloaked figure laying dead on the ground, you finally get a look at his face. On his face you recognize a tattoo. You remember the tattoo from a cultist group that is known for using the dark arts.")
            choice2 = input("Do you wish to look around your farm? (y/n) ")
            print()
            if choice2 == "yes" or choice2 == "y":
                gold += 20
                dprint("You start to look around your farm for any other people, but find medical supplies and 20 gold instead. So you decided to heal yourself. You are now fully healed.")
                print("You have", gold, "gold.")
                player_hp = maxhp
                pitchfork = input("In addition to your medicine, you found a pitchfork. Do you want to pick it up? (y/n) ")
                if pitchfork == "yes" or pitchfork == "y":
                    x = 2
                    inventoryw["pitchfork"] = 2
                print()
                dprint("You also find a cultist snooping around your farm, and to your luck he doesn't see you.")
                choice3 = input("Do you want to follow the cultist? (y/n) ")
                print()
                if choice3 == "yes" or choice3 == "y":
                    dprint("You end up secretly following the cultist back to his lair, but you encounter a guard outside. The guard attacks you!")
                    enemy_hp = random.randint (40, 55)
                    enemy_damage = 6
                    player_hp = fight(player_hp, enemy_hp)
                    if player_hp <= 0:
                        dprint("The guard has bested you. You are dead. GAME OVER!!!")
                        lives = 0
                    elif player_hp > 0:
                        print()
                        dprint("Somehow you were able to take out the guard. He had 40 gold. You sneaked into the hideout without getting caught.")
                        gold += 40
                        print("You now have", gold, "gold.")
                        sword = input("You quietly search around the hideout and find some bread and a spear. You eat the bread and feel awesome. Do you want to pick up the spear? (y/n) ")
                        player_hp = maxhp
                        if sword == "y" or sword == "yes":
                            x = 3
                            inventoryw["spear"] = 3
                        print()
                        dprint("After you search the hideout, you go out the back and find a shack. You find the cultist leader inside and she slashes at you first")
                        enemy_hp = random.randint(80, 100)
                        enemy_damage = 7
                        player_hp = fight(player_hp, enemy_hp)
                        print()
                        if player_hp <= 0:
                            dprint("The cultist leader slices your throat. You fall down dead. GAME OVER!!!")
                            lives = 0
                        elif player_hp > 0:
                            dprint("You have slain the cultist leader, and took down their regime.")
#                             print("Congratulation, you have beaten my game. Well done, here is you prize, a giant cookie that you can't eat!!!")
                            print()
                            dprint("After you successfully slew the cult, you went home and thought about what had happened. You ventured into your house, and on the ground you found a book that was left from on of the cultists.")
                            player_hp = maxhp
                            book = input("Do you want to open and read the book? (y/n) ")
                            print()
                            if book == "yes" or book == "y":
                                dprint("By opening the book, you read and recite an old cantation. Not long after, a fallen star appears in front of you and leads you to a small cave. Before you know it, you are in a fight with a cultist who wanted revenge.")
                                enemy_hp = random.randint(60, 80)
                                fight(player_hp, enemy_hp)
                                if player_hp <= 0:
                                    dprint("Wow, you died to a petty minion. Shame on you. GAME OVER!!!")
                                    lives = 0
                                elif player_hp > 0:
                                    dprint("You bested the minion, and are able to explore the cave. You find a steel sword.")
                                    sword2 = input("Do you want to pick up the steel sword? (y/n) ")
                                    if sword2 == "yes" or sword2 == "y":
                                        x = 4
                                        inventoryw["steel sword"] = 4
                                    dprint("You leave the cave and return home to rest")
                                    player_hp = maxhp
                            elif book == "no" or book == "n":
                                dprint("You put the book away.")
                                search = input("Do you want to continue exploring the farm? (y/n) ")
                                if search == "yes" or search == "y":
                                    dprint("You looked around in the barn and found that the whole place had been sacked. Under the remains you found a cloak.")
                                    cloak = input("Do you want to pick up the cloak? (y/n) ")
                                    if cloak == "yes" or cloak == "y":
                                        dprint("Your base health has increased by 15")
                                        maxhp += 15
                                        inventoryc["cloak"] = 15
                                        player_hp = maxhp
                                elif search == "no" or search == "n":
                                    dprint("You go back to bed.")
                                else:
                                    dprint("Fine, give the wrong anwser then.")
                            else:
                                dprint("You made it this far and just threw away your sword and or cloak.")
                            dprint ("Now you clean up your barn and put everything back to normal.")
                            dprint("Eventually, go are able to go back to bed, and in the morning, you decide there are two choices: To see if there are any more cults, or learn more about the cult that wasn't so great.")
                            choice8 = input("Do you want to search or learn? ")
                            if choice8 == "search":
                                choice8 = "search"
                            elif choice8 == "learn":
                                choice8 = "learn"
                            else:
                                dprint("Don't do this to me, please say search, never mind. I'll pick.")
                                n = random.randint(1, 2)
                                if n == 1:
                                    choice8 = "search"
                                else:
                                    choice8 = "learn"
                            dprint("Well, either way, you have to start somewhere, and that somewhere is back in town. Now you are on your guard, just in case something was to happen.")
                            robber = random.randint(1,10)
                            if robber <= 4:
                                enemy_damage = 8
                                dprint("So much for being careful, an armed robber has followed you and ambushed you.")
                                enemy_hp = random.randint(70, 85)
                                player_hp = fight(player_hp, enemy_hp)
                                if player_hp <= 0:
                                    dprint("I really thought you were going to be a hero, maybe I'll give you a second chance... Fine. I'll do it. Don't let this happen again.")
                                    player_hp = maxhp
                                    dprint("Now that the robber almost made you mincemeat, you finally make it back onto your feet")
                                else:
                                    dprint("The robber had a helmet and 80 gold. He didn't have much else.")
                                    choice9 = input("Do you want to pick up the helmet? (y/n) ")
                                    if choice9 == "yes" or choice9 == "y":
                                        maxhp += 30
                                        player_hp = maxhp
                                        dprint("Your maxhp has increased by 30!")
                                        inventoryc["helmet"] = 30
                                    choice10 = input("Do you want to pick up the 80 gold? (y/n) ")
                                    if choice10 == "yes" or choice10 == "y":
                                        gold += 80
                                        print("You have", gold, "gold")
                            dprint("Now that you are on your way into town, you can either go to the general store or to the town hall and ask around.")
                            choice11 = input("Do you want to go the general store or the town hall? ")
                            if choice11 == "general store":
                                dprint("So you decide to go to the general store.")
                                shop(gold, SHOPW, SHOPC)
                                if choice8 == "search":
                                    dprint("You eventually go to the town hall and find the mayor. He was busy, so you can't talk to him now. The secretart asked why you needed to talk to him, and you told her about your experience with the cult. She hushed you, and said that it wasn't safe to talk about it in the open. She proceeded to take you into an empty room and said that there were many other cults, escpecially in the vally regions.")
                                else:
                                    dprint("The mayor was convieniently free and agreed to see you. You asked him about the cult and if there were any more of them. He replied with a chuckle, and said there are many cults, and the one that you ended was only one of the smallest, or so he has heard. He doesn't know much more about the cult itself, other than there was another located in the mountians somewhere.")
                                dprint("With what little information you gathered, you left the town hall, and returned to the center of the town.")
                                find = random.randint(1,6)
                                if find >= 3:
                                    dprint("You find 30 gold on the ground.")
                                    gold += 30
                                    print("You have", gold, "gold")
                                choice12 = input("Do you want to look around for clues or go to the general store? (clues/general store) ")
                                if choice12 == "general store":
                                    shop(gold, SHOPW, SHOPC)
                            elif choice11 == "town hall":
                                if choice8 == "search":
                                    dprint("You go to the town hall and find the mayor. He was busy, so you can't talk to him now. The secretart asked why you needed to talk to him, and you told her about your experience with the cult. She hushed you, and said that it wasn't safe to talk about it in the open. She proceeded to take you into an empty room and said that there were many other cults, escpecially in the vally regions.")
                                else:
                                    dprint("The mayor was convieniently free and agreed to see you. You asked him about the cult and if there were any more of them. He replied with a chuckle, and said there are many cults, and the one that you ended was only one of the smallest, or so he has heard. He doesn't know much more about the cult itself, other than there was another located in the mountians somewhere.")
                                dprint("With what little information you gathered, you left the town hall, and returned to the center of the town.")
                                find = random.randint(1,6)
                                if find >= 3:
                                    dprint("You find 30 gold on the ground.")
                                    gold += 30
                                    print("You have", gold, "gold")
                                choice12 = input("Do you want to look around for clues or go to the general store? (clues/general store) ") 
                                if choice12 == "general store":
                                    shop(gold, SHOPW, SHOPC)
                elif choice3 == "no" or choice3 == "n":
                    dprint("Ok, so you decided not to chase him, and you go into town instead.")
                    dprint("You ask around town about the cult, but nobody gives you any leads. After three hours of asking, you finally find an old man who says he knows where the cult group is located.")
                    choice7 = input("He offers you a suspicious map. Do you accept it? (y/n) ")
                    print()
                    if choice7 == "yes" or choice7 == "y":
                        dprint("You follow the map and find an abandoned house on the edge of a cliff.")
                        dprint("As you look off over the cliffside, you are shoved off and plummit to your death. GAME OVER!!!")
                    elif choice7 == "no" or choice7 == "n":
                        dprint("The man who offered you the map reveals his tattoo and jumps at you!")
                        enemy_hp = random.randint(20, 40)
                        enemy_damage = 4
                        player_hp = fight(player_hp, enemy_hp)
                        print()
                        if player_hp <= 0:
                            dprint("Really? You were killed by an old man? Oh well, we have all seen better days. GAME OVER!!!")
                            lives = 0
                        elif player_hp > 0:
                            gold += 30
                            dprint("You drop the dead man on the ground. You step over the man and the map and go into the house, and you find a spear on the wall and 30 gold.") 
                            print("You now have", gold, "gold.")
                            spear = input("Do you want to take the spear? (y/n) ")
                            print()
                            if spear == "yes" or spear == "y":
                                x = 3
                                inventoryw["spear"] = 3
                            dprint("You continue to look around the house, and you find a picture of a woman. On the bottom of the picture was written, 'In the shack by the woods'.")
                            picture = input("Do you want to pick up the picture? (y/n) ") #Put in a story branch for the picture
                            print()
                            dprint("You don't find anything else of use except for some potatos, and then you leave the house. You eat them and feel better, but don't know where to go now. You decide that you can either go to the general store or visit your friend and tell him about what is going on.")
                            player_hp = maxhp
                            gs = input("Do you want to go to the general store or not? (y/n) ")
                            print()
                            if gs == "yes" or gs == "y":
                                dprint("You sucsessfully make it to the general store and ask the clerk about the cult. He says that he knows some things, but it will be for a price.")
                                print()
                                info = input("Do you want to pay 30 gold to find out more about the cult? (y/n) ")
                                if info == "yes" or info == "y":
                                    gold -= 30
                                    print()
                                    print("You now have", gold, "gold.") 
                                    dprint("The clerk leads you to a table in the corner of the room, and starts to tell you about the cult. He says that the cult has been around as long as anyone can remember, and it is constantly growing. The leader of the cult is an evil witch who takes over people's lives and souls.")
                                    dprint("He tells you that the cult is located in the forest, but there were rumors that they were moving to the mountians to spread their power. They possess powers that are great and powerful, but they are originated from evil means. Once people get sucked in, they never leave.")
                                    dprint("That was all he knew, and he asked if you wanted to look around or buy anything.")
                                else:
                                    print()
                                    store = input("Do you wish to look around the store? (y/n) ")
                                    print()
                                    if store == "yes" or store == "y":
                                        shop(gold, SHOPW, SHOPC)
                            elif gs == "no" or gs == "n":
                                if picture == "yes" or picture == "y":
                                    dprint("So you decided to visit your friend. He lives in the center of town and on your way there, you encounter a man on the street corner who is selling watches. He says that you can have a watch if you give him something in return. You hand him the picture of the woman and run off with the watch.") 
                                    print("Your max hp is now", maxhp)
                                    maxhp += 10
                                    player_hp = maxhp
                                    inventoryc["watch"] = 10
                                elif picture == "no" or picture == "n":
                                    dprint("So you decided to visit your friend. He lives in the center of town and on your way there, you encounter a man on the street corner who is selling watches. He stops you and asks you if you want a watch. It costs 100 gold.")
                                    print()
                                    man = input("Do you want to buy a watch? (y/n) ")
                                    print()
                                    if man == "yes" or man == "y":
                                        if gold >= 100:
                                            gold -= 100
                                            maxhp += 10
                                            player_hp = maxhp
                                            inventoryc["watch"] = 10
                                            dprint("You bought a watch that increased your max hp by 10!")
                                    elif man == "no" or man == "n":
                                        dprint("The man is dissapointed that you didn't buy a watch, but he said he understands.")
                                    else:
                                        dprint("The man is offended that you didn't anwser his question correctly. He kicks you harder than you expected. You lost 10 hp.")
                                        player_hp -= 10
                                dprint("You finally make it to your frinds house, but the front door was ajar. You call for him, but nobody anwsers. Instead, a bulky man steps out and swings a club at you!")
                                print()
                                enemy_hp = random.randint(60, 80)
                                fight(player_hp, enemy_hp)
                                print()
                                if player_hp <= 0:
                                    dprint("The large man has clobbered you and now you are dead! GAME OVER!!!")
                                    lives = 0
                                elif player_hp > 0:
                                    dprint("You have slain the large man!")
                            else:
                                dprint("Make up your mind already... Whatever. GAME OVER!!!")
                                lives = 0
                    else:
                        dprint("If you can't make a simple decision on whether or not to take a map, I can't have you finish my game. GAME OVER!!!")
                        lives = 0
                else:
                    print("Just make up your mind already. You know what, I'm done with this", name,"GAME OVER!!!")
                    lives = 0
            elif choice2 == "no" or choice2 == "n":
                dprint("You chose to go back to bed and sleep.")
                sleep = random.randint(1, 7)
                if sleep == 1:
                    dprint("You never woke up. GAME OVER!!!")
                    lives = 0
                else:
                    dprint ("You wake up feeling better than you did yesterday.")
                    player_hp += 20
                    dprint ("You notice a dark figure sitting in the corner of your dimmly lit room. She jumps out and attacks.")
                    print()
                    enemy_hp = random.randint(30, 50)
                    player_hp = fight(player_hp, enemy_hp)
                    print()
                    if player_hp <= 0:
                        dprint("You met your match with the dark figure. GAME OVER!!!")
                        lives = 0
                    elif player_hp > 0:
                        dprint("The sun is rising, which allows you to see her face. So you decide to look, and you notice that she bares the same tattoo. Also, she had 40 gold on her, so why not take it.")
                        gold += 40
                        print("You have", gold, "gold.")
                        choice4 = input("Do you want to go to go to the town and ask around about the cult? (y/n)")
                        print()
                        if choice4 == "yes" or choice4 == "y":
                            if player_hp < 20:
                                dprint("You are able to crawl into town, but need medical attention.")
                                choice5 = input("A stranger confronts you and asks if you want his medicine. (y/n) ")
                                dprint()
                                if choice5 == "yes" or choice5 == "y":
                                    dprint("The stranger gives you his medication and you feel better imediately. You are now fully healed.")
                                    player_hp = maxhp
                                elif choice5 == "no" or choice5 == "n":
                                    dprint("You refused the medicine and died. GAME OVER!!!")
                                    lives = 0
                                else:
                                    dprint("I don't know if you were so injured that you couldn't think clearly or if you are just stupid, but either way, you didn't get the medicine. GAME OVER!!!")
                                    lives = 0
                                dprint("You asked the stranger about the cultists, and he told you of someone who used to be involed in the cult. Her name was Sugo.")
                                dprint("You decided to go visit Sugo, and you found her in a little shack. You talk for a while, and you found out that she was still part of the cult. She gives you the offer to join.")
                                choice6 = input("Do you want to join Sugo and the cult? (y/n) ")
                                print()
                                if choice6 == "yes" or choice6 == "y":
#                                   print("So you joined the cult. Congratulations, you get the cultist ending, you phsycopath!")
                                    dprint("For a reward of joining the cult, Sugo offers you a steel sword")
                                    print()
                                    b_sword = input("Do you want to take the steel sword? (y/n) ")
                                    if b_sword == "yes" or b_sword == "y":
                                        x = 4
                                        inventoryw["steel sword"] = 4
                                    print()
                                    dprint("After she offers you the spear, she says that she is the leader of the cult. You are baffled.")
                                    print()
                                    betray = input("Do you want to betray her (y/n) ")
                                    print()
                                    if betray == "y" or betray == "yes":
                                        dprint("You have decided to turn against her and fight for the place of leader of the cult.")
                                        enemy_hp = random.randint(80, 100)
                                        enemy_damage = 7
                                        fight(player_hp, enemy_hp)
                                        if player_hp <= 0:
                                            print("You have been slain by Sugo, the true leader of the cult", name, "GAME OVER!!!")
                                            lives = 0
                                        elif player_hp > 0:
                                            dprint("Sugo, now laying on the ground, has been taken out, and you are now the leader of the cult. Everyone is now in your command, and you have power over the whole cult.")
                                            print()
                                            dprint("As your first act as leader of the cult, you decide to find out about other cults and decide if you want to try to build allies or take control of the cults.")
                                            allies = input("Do you want to make allies or take over other cults? (allies/take) ")
                                            if allies == "allies":
                                                dprint("Fill this gap with something")
                                            elif allies == "take":
                                                dprint("Fill this with something else.")
                                    elif betray == "n" or betray == "no":
                                        dprint("Since you are now under Sugo, she has you go after the last person who tried to kill her. His name is Hank. Sugo said the last time he was seen was two years ago at the train station.")
                                        print()
                                        gold += 300
                                        dprint("Sugo sends you off to the train station to find out more about Hank and where he went. She also sent you with 300 gold just in case.") 
                                        print("You now have", gold, "gold.")
                                    else:
                                        print("What are you doing here", name, "you lazy bum, get out of here! GAME OVER!!!")
                                        lives = 0
                                elif choice6 == "no" or choice6 == "n":
                                    dprint("Sugo said you knew too much, and you were executed on the spot. GAME OVER!!!")
                                    lives = 0
                                else:
                                    dprint("You lazy turd, you didn't do as I said. Leave my game! GAME OVER!!!")
                                    lives = 0
                        elif choice4 == "no" or choice4 == "n":
                            dprint("You fall back in bed, exausted from the fighting. The cultists have decided to leave you alone since you have slayed two of their members.")
                            print("You win the lazy award", name, "for just wanting to sleep.", '"Congratulations" on being so lazy you do not even want to get out of bed!')
                            lives = 0
                        else:
                            dprint("Well then, I guess you lost interest in playing my game correctly. I am just going to kill you now. GAME OVER!!!")
                            lives = 0
            else:
                print(name, "get your act together. Is this how you wanted your story to end? Fine, I'll end it. GAME OVER!!!")
                lives = 0
    elif choice1 == "no" or choice1 == "n":
        dprint ("You go to sleep and never wake up. GAME OVER!!!")
        lives = 0
    else:
        print ("Well", name,"you didn't put yes or no, sooooo... you just stood there and died. GAME OVER!!!")
        lives = 0
print()
stats(p_total_dmg, dmg_taken, total_heals, t_dmg_counter, dmg_taken_counter, t_h_counter, turns_taken)
