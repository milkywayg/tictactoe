#!/usr/bin/env python3
import numpy as np
import os
import random as rn
import tictactoe_lib as tl


'''
start by defining a class of states with methods:
    -print the state
    -is winner
    -is looser
    -is draw
    -next state given the action 
'''

ms=3

def cls():
   os.system('clear') 


def rand_policy(game):
    return game.free_pos()[rn.randrange(len(game.free_pos()))]


#====== main =======
game=tl.ttt_cl()
pos=9
while not game.game_done():
    cls()
    game.draw()
    while (not(pos in game.free_pos())):
        pos_s = input("Enter a position:")
        pos=int(pos_s)
    #player
    game.ply_action(pos=pos,plyr=-1)
    #computer
    if (not game.game_done()):
        pos_comput=rand_policy(game)
        game.ply_action(pos=pos_comput,plyr=1)


cls()
game.draw()
if (game.is_winner(1)):
    print("You loose :-(")
else:
    print("You WIIIIN!! :-)")
print()










