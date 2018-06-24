#!/usr/bin/env python3
import numpy as np
import os
import random as rn
import tictactoe_lib as tl
import pickle


'''
start by defining a class of states with methods:
    -print the state
    -is winner
    -is looser
    -is draw
    -next state given the action 
'''

ms=tl.ms

def cls():
   os.system('clear') 


def rand_policy(game):
    return game.free_pos()[rn.randrange(len(game.free_pos()))]

f = open('q_func.p', 'rb')
q_best= pickle.load(f)
f.close()


def q_policy(game):
    s_idx=tl.fstate.tolist().index(game.state.flatten().tolist())
    q_state=q_best[s_idx]
    q_pos=np.argmax(q_state)
    if (q_pos in game.free_pos()):
        return q_pos
    else:
        #  print('-------')
        return rand_policy(game)


#====== main =======
game=tl.ttt_cl()
pos=9
cpu_first=rn.randrange(2)
while not game.game_done():
    cls()
    if (cpu_first==0):
        game.draw()
        while (not(pos in game.free_pos())):
            pos_s = input("Enter a position:")
            pos=int(pos_s)
        #player
        game.ply_action(pos=pos,plyr=-1)
        #computer
        if (not game.game_done()):
            #  pos_comput=rand_policy(game)
            pos_comput=q_policy(game)
            game.ply_action(pos=pos_comput,plyr=1)
    else:
        #computer
        if (not game.game_done()):
            #  pos_comput=rand_policy(game)
            pos_comput=q_policy(game)
            game.ply_action(pos=pos_comput,plyr=1)
            game.draw()
            if (not game.game_done()):
                pos_s = input("Enter a position:")
                pos=int(pos_s)
                while (not(pos in game.free_pos())):
                    pos_s = input("Enter a position:")
                    pos=int(pos_s)
                #player
                game.ply_action(pos=pos,plyr=-1)

cls()
game.draw()
if (game.is_winner(1)):
    print("You loose :-(")
elif (game.is_winner(-1)):
    print("You WIIIIN!! :-)")
elif (game.game_done()):
    print("Draw")

print()










