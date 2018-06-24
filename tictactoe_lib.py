#!/usr/bin/env python3
import numpy as np
from copy import copy, deepcopy


ms=2

class ttt_cl:
    #the state is represented by a 3x3 matrix
    #0 means empty case, 1 is X from the cpu, 0 is O from the opponent
    #  state=np.zeros((ms,ms))
    def __init__(self,state=[]):
        if (state==[]):
            self.state=np.zeros((ms,ms))
        else:
            self.state=np.copy(state) # np.reshape(np.asarray(state),(3,3))

    def is_winner(self, plyr=1):
        s=self.state
        dg0=[s[ii,ii] for ii in range(ms)]
        dg1=[s[ms-1-ii,ms-1-ii] for ii in range(ms)]
        line_sum=[s.sum(axis=0),s.sum(axis=1)]
        line_sum_l=np.concatenate(line_sum).ravel().tolist()+[sum(dg0)]+[sum(dg1)]
        return (plyr*ms) in line_sum_l

    def no_winner(self):
        return not (self.is_winner(1) or self.is_winner(-1))

    def game_done(self):
        comput_win=self.is_winner(1)
        plyr_win=self.is_winner(-1)
        s=self.state
        return (not(0 in s) or comput_win or plyr_win)

    #capture the fact that the game should be balanced in X and 0
    def is_bad_state(self):
        if (abs(np.sum(self.state))==1 or abs(np.sum(self.state))==0):
            return 0
        else:
            return 1

    #pos is a number from 0-8
    def ply_action(self, pos=0, plyr=1):
        s=self.state
        sf=s.flatten()
        if (pos<0 or pos>((ms**2)-1)):
            return 1 #error
        else:
            if (np.sum(self.state)==1):
                return 1 #error bad action get out of balance
            if (sf[pos]==0):
                sf[pos]=plyr
                self.state=np.reshape(sf,(ms,ms))
                return 0
            else:
                return 1

    def draw(self):
        s=self.state
        print()
        print()
        for idx_ln, ln in enumerate(s):
            print(' '*30,end=' ')
            print('|',end=' ')
            for idx_col, val in enumerate(ln):
                pos=idx_ln*ms+idx_col
                #this case is empty
                if (s[idx_ln,idx_col]==0):
                    print(repr(pos).center(3),end='|')
                elif (s[idx_ln,idx_col]==1):
                    print('X'.center(3),end='|')
                elif (s[idx_ln,idx_col]==-1):
                    print('O'.center(3),end='|')
            print('')

    def free_pos(self):
        s=self.state
        sf=s.flatten()
        free=np.where(sf==0)
        return free[0].tolist()

    def free_pos_bm(self):
        s=self.state
        sf=s.flatten()
        return sf==0




def cartesian(arrays, out=None):
    """
    Generate a cartesian product of input arrays.
    Parameters
    ----------
    arrays : list of array-like
        1-D arrays to form the cartesian product of.
    out : ndarray
        Array to place the cartesian product in.
    Returns
    -------
    out : ndarray
        2-D array of shape (M, len(arrays)) containing cartesian products
        formed of input arrays.
    Examples
    --------
    >>> cartesian(([1, 2, 3], [4, 5], [6, 7]))
    array([[1, 4, 6],
           [1, 4, 7],
           [1, 5, 6],
           [1, 5, 7],
           [2, 4, 6],
           [2, 4, 7],
           [2, 5, 6],
           [2, 5, 7],
           [3, 4, 6],
           [3, 4, 7],
           [3, 5, 6],
           [3, 5, 7]])
    """

    arrays = [np.asarray(x) for x in arrays]
    dtype = arrays[0].dtype

    n = np.prod([x.size for x in arrays])
    if out is None:
        out = np.zeros([n, len(arrays)], dtype=dtype)

    m = int(n / arrays[0].size)
    out[:,0] = np.repeat(arrays[0], m)
    if arrays[1:]:
        cartesian(arrays[1:], out=out[0:m,1:])
        for j in range(1, arrays[0].size):
            out[j*m:(j+1)*m,1:] = out[0:m,1:]
    return out



vs=[-1,0,1]
num_state=(len(vs))**(ms**2)
num_action=ms**2
fstate=cartesian((vs,vs,vs,vs)) #,vs,vs,vs,vs,vs)) 









