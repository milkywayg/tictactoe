#!/usr/bin/env python3
import numpy as np
import os
import tictactoe_lib as tl


def reward(game, action_pos=0):
    t_game=game
    t_game.ply_action(pos=action_pos,plyr=1)
    if (t_game.is_winner(plyr=1)):
        return 1
    else:
        return 0


#Q-function is vector of 9 + 1 (state+action)

qinit=np.zeros((tl.num_state,tl.num_action))

def bellman_1_step_iter(q):
    #compute max_a' Q(s',a')
    idx=0
    m_q=[]
    for line in q:
        m_q[idx]=max(line) 
        idx+=1
    nxt_q=qinit
    for st in range(tl.num_state):
        for at in range(tl.num_action):
            #compute next state- s'
            cs_arr=tl.fstate[st]
            cs_cl=tl.ttt_cl(cs_arr)
            ns_cl=cs_cl.ply_action(pos=at,plyr=1)
            ns_arr=ns_cl.state.flatten()
            
            




















