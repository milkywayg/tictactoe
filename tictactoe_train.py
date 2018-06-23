#!/usr/bin/env python3
import numpy as np
import os
import tictactoe_lib as tl


def reward(game, action_pos=0):
    t_game=game
    t_game.ply_action(place=action_pos,plyr=1)
    if (t_game.is_winner(plyr=1)):
        return 1
    else:
        return 0


#Q-function is vector of 9 + 1 (state+action)

qinit=np.zeros((tl.num_state,tl.num_action))

def bellman_1_step_iter(q):
    
    

















