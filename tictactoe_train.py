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
    t_game=deepcopy(game)
    err=t_game.ply_action(pos=action_pos,plyr=1)
    if (err==1):
        return -1
    if (t_game.is_winner(plyr=1)):
        return 1
    else:
        return 0


#Q-function is vector of 9 + 1 (state+action)

qinit=np.zeros((tl.num_state,tl.num_action))
ms=tl.ms

def bellman_1_step_iter(q):
    #compute max_a' Q(s',a')
    idx=0
    m_q=[]
    for line in q:
        m_q=m_q+[max(line)]
        idx+=1
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
#              if (st%1000==0):
#                  print(str(st)+" and "+str(at))
                rwd=reward(game=cs_cl,action_pos=at)
                if (rwd==-1):#the action is not legal
                    nxt_q[st,at]=big_neg
                else:
                    #compute next state- s'
                    ns_cl=deepcopy(cs_cl)
                    ns_cl.ply_action(pos=at,plyr=1)
                    ns_arr=ns_cl.state.flatten()
                    ns_idx=tl.fstate.tolist().index(ns_arr.tolist())
                    nxt_q[st,at]=rwd+m_q[ns_idx]
    return nxt_q

def bellman_iter():
    q=np.copy(qinit)
    eps=1e-3
    err=1
    idx=0
    while err>eps:
        print("---- Iteration number ="+str(idx))
        n_q=bellman_1_step_iter(q)
        n_err_arr=np.absolute(n_q-q)
        n_err=np.amax(n_err_arr)
        summ=np.sum(n_err_arr)
        err=n_err
        print("==== Iteration #"+str(idx)+" error="+str(err)+" sum="+str(summ))
        q=np.copy(n_q)
        idx+=1
    return q

#====================
q_end=bellman_iter()


f = open('q_func.p', 'wb')
pickle.dump(q_end, f)
f.close()

        



















