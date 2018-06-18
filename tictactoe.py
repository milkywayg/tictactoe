#!/usr/bin/env python3
import numpy as np

#  for ii in range(0,5):
#      print ("line number="+str(ii))
#
#
#  for uu in range(0,45):
#      print ("line number="+str(uu))




'''
start by defining a class of states with methods:
    -print the state
    -is winner
    -is looser
    -is draw
    -next state given the action 
'''

ms=3
class ttt_cl:
    #the state is represented by a 3x3 matrix
    #0 means empty case, 1 is X from the cpu, 0 is O from the opponent
    #  state=np.zeros((ms,ms))
    def __init__(self):
        self.state=np.zeros((ms,ms))

    def is_winner(self, plyr=1):
        s=self.state
        dg0=[s[ii,ii] for ii in range(ms)]
        dg1=[s[2-ii,2-ii] for ii in range(ms)]
        line_sum=[s.sum(axis=0),s.sum(axis=1),s.sum(axis=2)]
        line_sum_l=np.concatenate(line_sum).ravel().tolist()+[dg0.sum()]+[dg1.sum()]
        return (plyr*ms) in line_sum_l

    def no_winner(self):
        return not (self.is_winner(1) or self.is_winner(-1))

    def game_done(self):
        s=self.state
        return not(0 in s)
    def ply_action(self, place=0, plyr=1):
        





















