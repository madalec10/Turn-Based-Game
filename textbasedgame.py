#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:01:03 2018

@author: stem
"""

import random
player_hp = 60
enemy_hp = random.randint(40, 70)
x = 1
p_total_dmg = 0
t_dmg_counter = 0
dmg_taken = 0
dmg_taken_counter = 0
total_heals = 0
t_h_counter = 1
turns_taken = 0

def enemy_atk(php):
    global dmg_taken
    global dmg_taken_counter
    miss_or_hit = random.randint(1, 3)
    if miss_or_hit == 1:
        print("Enemy missed")
    else:
        enemy_dmg = random.randint(3, 8)
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
            dmg = random.randint(3, 8)
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
    elif x == 2:
        roll = random.randint(1, 6)
        if roll < 2:
            print("You missed!")
        elif roll < 6:
            dmg = random.randint(5, 8)
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
        else:
            dmg = 11
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
    elif x == 3:
        roll = random.randint(1, 6)
        if roll < 3:
            print("You missed!")
        elif roll < 6:
            dmg = random.randint(4, 10)
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
        else:
            dmg = 13
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
    elif x == 4:
        roll = random.randint(1, 6)
        if roll < 3:
            print("You missed!")
        elif roll < 6:
            dmg = random.randint(5, 12)
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
        else:
            dmg = 15
            ehp = ehp - dmg
            print("You dealt", dmg, "damage!")
            p_total_dmg += dmg
            t_dmg_counter += 1
    return ehp

def player_heal(health):
    global total_heals
    global t_h_counter
    roll = random.randint(1, 6)
    if health >= 58:
        print("Health is full")
    elif roll == 1:
        print("Your heal failed!")
    elif roll < 6:
        heal = random.randint(2, 6)
        print("You healed", heal, "hp!")
        health = heal + health
        total_heals += heal
        t_h_counter += 1
    else:
        heal = 10
        print("You healed 8 hp!!")
        health = heal + health
        total_heals += heal
        t_h_counter += 1
    return health

def fight(php, ehp):
    global turns_taken
    while php > 0 and ehp > 0:
        turns_taken += 1
        print("Your health is", php)
        print("Enemy's health is", ehp)
        a = input("Press 1 for Attack,Press 2 for heal." )
        if a.isdigit() == True:
            a = float(a)
        php = enemy_atk(php)
        if a == 1 and php > 0:
            ehp = player_atk(ehp, x)
        elif a == 2 and php > 0:
            php = player_heal(php)
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
        avg_dealt = p_dmg / p_counter
        avg_taken = dmg_tak / taken_counter
        avg_heal = t_heals / h_counter
        print("Your average damage dealt was", avg_dealt)
        print("Your average damage taken was", avg_taken)
        print("Your average heal was", avg_heal)
        print("You had", turns,"turns this round")

name = input("Please enter your name: ")
while name == "":
    name = input("Please enter your name, I am losing my patience: ")
print()
print ("You wake up to a loud crash outside your home. It is quiet for a moment, but then there is another loud bang. You don’t know what is out there, so you grab your sword and some food and venture outside to see what the noise was. A cloaked figure is ransacking your farm and stealing your store for the winter.")
choice1 = input("Do you wish to investigate? (y/n) ")
print()
if choice1 == "y" or choice1 == "yes":
    print ("The cloaked figure has attacked you!")
    player_hp = fight(player_hp, enemy_hp)
    if player_hp <= 0:
        print("You were killed by the cloaked figure. GAME OVER!!!")
    elif player_hp > 0:
        print()
        print("With the cloaked figure laying dead on the ground, you finally get a look at his face. On his face you recognize a tattoo. You remember the tattoo from a cultist group that is known for using the dark arts.")
        choice2 = input("Do you wish to look around your farm? (y/n) ")
        print()
        if choice2 == "yes" or choice2 == "y":
            print("You start to look around your farm for any other people, but find medical supplies instead. So you decided to heal yourself. You are now fully healed.")
            player_hp = 60
            pitchfork = input("In addition to your medicine, you found a pitchfork. Do you want to pick it up? (y/n) ")
            if pitchfork == "yes" or pitchfork == "y":
                x = 2
            print()
            print("You also find a cultist snooping around your farm, and to your luck he doesn't see you.")
            choice3 = input("Do you want to follow the cultist? (y/n) ")
            print()
            if choice3 == "yes" or choice3 == "y":
                print("You end up secretly following the cultist back to his lair, but you encounter a guard outside. The guard attacks you!")
                enemy_hp = random.randint (40, 55)
                player_hp = fight(player_hp, enemy_hp)
                if player_hp <= 0:
                    print("The guard has bested you. You are dead. GAME OVER!!!")
                elif player_hp > 0:
                    print()
                    print("Somehow you were able to take out the guard, and you sneaked into the hideout.")
                    sword = input("You quietly search around the hideout and find some bread and a buster sword. You eat the bread and feel awesome. Do you want to pick up the buster sword? (y/n) ")
                    player_hp = 60
                    if sword == "y" or sword == "yes":
                        x = 3
                    print()
                    print("After you search the hideout, you go out the back and find a shack. You find the cultist leader inside and she slashes at you first")
                    enemy_hp = random.randint(80, 100)
                    player_hp = fight(player_hp, enemy_hp)
                    print()
                    if player_hp <= 0:
                        print("The cultist leader slices your throat. You fall down dead. GAME OVER!!!")
                    elif player_hp > 0:
                        print("You have slain the cultist leader, and took down their regime.")
#                        print("Congratulation, you have beaten my game. Well done, here is you prize, a giant cookie that you can't eat!!!")
                        print()
                        print("After you successfully slew the cult, you went home and thought about what had happened. You ventured into your house, and on the ground you found a book that was left from on of the cultists.")
                        player_hp = 60
                        book = input("Do you want to open and read the book? (y/n) ")
                        print()
                        if book == "yes" or book == "y":
                            print("By opening the book, you read and recite an old cantation. Not long after, a fallen star appears in front of you and leads you to a small cave. Before you know it, you are in a fight with a cultist who wanted revenge.")
                            enemy_hp = random.randint(60, 80)
                            fight(player_hp, enemy_hp)
                            if player_hp <= 0:
                                print("Wow, you died to a petty minion. Shame on you. GAME OVER!!!")
                            elif player_hp > 0:
                                print("You bested the minion, and are able to explore the cave. You find a diamond plated sword.")
                                sword2 = input("Do you want to pick up the diamond plated sword? (y/n) ")
                                if sword2 == "yes" or sword2 == "y":
                                    x = 4
                                print("You leave the cave and return home to rest")
                                player_hp = 60
                        elif book == "no" or book == "n":
                            print("You put the book away.")
                            search = input("Do you want to continue exploring the farm? (y/n) ")
                            if search == "yes" or search == "y":
                                print("You looked around in the barn and found that the whole place had been sacked. Under the remains you found a cloak.")
                                cloak = input("Do you want to pick up the cloak? (y/n) ")
                                if cloak == "yes" or cloak == "y":
                                     print("Your base health has increased by 15")
                                     player_hp = 75
                            elif search == "no" or search == "n":
                                print("You go back to bed.")
                            else:
                                print("Fine, give the wrong anwser then.")
                        else:
                            print("You made it this far and just threw away your sword and or cloak.")
                        print ("Now you clean up your barn and put everything back to normal.")
                        
            elif choice3 == "no" or choice3 == "n":
                print("Ok, so you decided not to chase him, and you go into town instead.")
                print("You ask around town about the cult, but nobody gives you any leads. After three hours of asking, you finally find an old man who says he knows where the cult group is located.")
                choice7 = input("He offers you a map. Do you accept it? (y/n) ")
                print()
                if choice7 == "yes" or choice7 == "y":
                    print("You follow the map and find an abandoned house on the edge of a cliff.")
                    print("As you look off over the cliffside, you are shoved off and plummit to your death. GAME OVER!!!")
                elif choice7 == "no" or choice7 == "n":
                    print("The man who offered you the map reveals his tattoo and jumps at you!")
                    enemy_hp = random.randint(20, 40)
                    player_hp = fight(player_hp, enemy_hp)
                    print()
                    if player_hp <= 0:
                        print("Really? You were killed by an old man? Oh well, we have all seen better days. GAME OVER!!!")
                    elif player_hp > 0:
                        print("You drop the dead man on the ground. Before you get a chance to look at the map, you were ambushed and executed. GAME OVER!!!")
                else:
                    print("If you can't make a simple decision on whether or not to take a map, I can't have finish my game. GAME OVER!!!")
                    
            else:
                print("Just make up your mind already. You know what, I'm done with this", name,"GAME OVER!!!")
            
        elif choice2 == "no" or choice2 == "n":
            print("You chose to go back to bed and sleep.")
            sleep = random.randint(1, 3)
            if sleep == 1:
                print("You never woke up. GAME OVER!!!")
            else:
                print ("You wake up feeling better than you did yesterday.")
                player_hp += 20
                print ("You notice a dark figure sitting in the corner of your dimmly lit room. She jumps out and attacks.")
                print()
                enemy_hp = random.randint(30, 50)
                player_hp = fight(player_hp, enemy_hp)
                print()
                if player_hp <= 0:
                    print("You met your match with the dark figure. GAME OVER!!!")
                elif player_hp > 0:
                    print("The sun is rising, which allows you to see her face. So you decide to look, and you notice that she bares the same tattoo.")
                    choice4 = input("Do you want to go to go to the town and ask around about the cult? (y/n)")
                    print()

                    if choice4 == "yes" or choice4 == "y":
                        print("You are able to crawl into town, but need medical attention.")
                        choice5 = input("A stranger confronts you and asks if you want his medicine. (y/n) ")
                        print()
                        if choice5 == "yes" or choice5 == "y":
                            print("The stranger gives you his medication and you feel better imediately. You are now fully healed.")
                            player_hp = 60
                            print("You asked the stranger about the cultists, and he told you of someone who used to be involed in the cult. Her name was Sugo.")
                            print("You decided to go visit Sugo, and you found her in a little shack. You talk for a while, and you found out that she was still part of the cult. She gives you the offer to join.")
                            choice6 = input("Do you want to join Sugo and the cult? (y/n) ")
                            print()
                            if choice6 == "yes" or choice6 == "y":
#                                print("So you joined the cult. Congratulations, you get the cultist ending, you phsycopath!")
                                print("For a reward of joining the cult, Sugo offers you a buster sword")
                                print()
                                b_sword = input("Do you want to take the buster sword? (y/n) ")
                                if b_sword == "yes" or b_sword == "y":
                                    x = 3
                                print()
                                print("After she offers you the sword, she says that she is the leader of the cult. You are baffled.")
                                print()
                                betray = input("Do you want to betray her (y/n) ")
                                print()
                                if betray == "y" or betray == "yes":
                                    print("You have decided to turn against her and fight for the place of leader of the cult.")
                                    enemy_hp = random.randint(80, 100)
                                    fight(player_hp, enemy_hp)
                                    if player_hp <= 0:
                                        print("You have been slain by Sugo, the true leader of the cult", name, "GAME OVER!!!")
                                    elif player_hp > 0:
                                        print("Sugo, now laying on the ground, has been taken out, and you are now the leader of the cult. Everyone is now in your command, and you have power over the whole cult.")
                                        print("")
                                elif betray == "n" or betray == "no":
                                    print("Since you are now under Sugo, she has you go after the last person who tried to kill her. His name is hank.")
                                else:
                                    print("What are you doing here", name, "you lazy bum, get out of here! GAME OVER!!!")
                            elif choice6 == "no" or choice6 == "n":
                                print("Sugo said you knew too much, and you were executed on the spot. GAME OVER!!!")
                            else:
                                print("You lazy turd, you didn't do as I said. Leave my game! GAME OVER!!!")
                                
                        elif choice5 == "no" or choice5 == "n":
                            print("You refused the medicine and died. GAME OVER!!!")
                        else:
                            print("I don't know if you were so injured that you couldn't think clearly or if you are just stupid, but either way, you didn't get the medicine. GAME OVER!!!")
                        
                    elif choice4 == "no" or choice4 == "n":
                        print("You fall back in bed, exausted from the fighting. The cultists have decided to leave you alone since you have slayed two of their members.")
                        print("You win the lazy award", name, "for just wanting to sleep.", '"Congratulations" on being so lazy you do not even want to get out of bed!')
                    else:
                        print("Well then, I guess you lost interest in playing my game correctly. I am just going to kill you now. GAME OVER!!!")
                   
        else:
            print(name, "get your act together. Is this how you wanted your story to end? Fine, I'll end it. GAME OVER!!!")
elif choice1 == "no" or choice1 == "n":
    print ("You go to sleep and never wake up. GAME OVER!!!")
else:
    print ("Well",name,"you didn't put yes or no, sooooo... you just stood there and died. GAME OVER!!!")
print()
stats(p_total_dmg, dmg_taken, total_heals, t_dmg_counter, dmg_taken_counter, t_h_counter, turns_taken)
