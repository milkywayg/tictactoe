#!/usr/bin/env python3
import numpy as np
import os
import tictactoe_lib as tl
import pickle
#  from copy import copy, deepcopy
from copy import deepcopy


#  f = open('test1.p', 'wb')
#  pickle.dump(tl.fstate, f)
#  f.close()


#  f = open('test1.p', 'rb')
#  ff= pickle.load(f)
#  f.close()

#  print(ff)

big_neg=-1000

def reward(game, action_pos=0):
    err, win, lose, end_game, nstate = game.nxt_states(action=action_pos)
    if (err==1):
        return [-10,[]] #should never go here
    if (win==1):
        return [1,[]]
    elif (lose==1):
        return [-1,[]]
    elif (end_game==1):
        return [0,[]]
    else:
        return [0,nstate]


#Q-function is vector of 9 + 1 (state+action)

qinit=np.zeros((tl.num_state,tl.num_action))
ms=tl.ms

def bellman_1_step_iter(q,gamma):
    #compute max_a' Q(s',a')
    idx=0
    nxt_q=np.copy(qinit)
    for st in range(tl.num_state):
        cs_arr=np.reshape(tl.fstate[st],(ms,ms))
        cs_cl=tl.ttt_cl(cs_arr)
#          if (st==39):
#              print('dd')
        if (cs_cl.game_done() or cs_cl.is_bad_state()):
            nxt_q[st,:]=np.zeros((1,tl.num_action))
        else:
            for at in range(tl.num_action):
                if (tl.fstate[st][at]!=0): #not a legal action
                    nxt_q[st,at]=big_neg
                else:
                    rwd,ns_idx_l=reward(game=cs_cl,action_pos=at)
                    #compute next state- s'
                    max_q_ns=[max(q[sidx,:]) for sidx in ns_idx_l]
                    if (rwd!=0):
                        nxt_q[st,at]=rwd
                    elif(max_q_ns==[]):
                        nxt_q[st,at]=0
                    else:
                        nxt_q[st,at]=gamma*np.array(max_q_ns).mean()
    return nxt_q

def bellman_iter(gamma):
    q=np.copy(qinit)
    eps=0.01
    err=1
    idx=0
    while err>eps:
        print("---- Iteration number ="+str(idx))
        n_q=bellman_1_step_iter(q,gamma)
        print("--Iteration #"+str(idx))
        print(n_q)
        n_err_arr=np.absolute(n_q-q)
        n_err=np.amax(n_err_arr)
        summ=np.sum(n_err_arr)
        err=n_err
        print("==== Iteration #"+str(idx)+" error="+str(err)+" sum="+str(summ))
        q=np.copy(n_q)
        idx+=1
    return q

#====================
gamma=1
q_end=bellman_iter(gamma)


f = open('q_func.p', 'wb')
pickle.dump(q_end, f)
f.close()

        



















