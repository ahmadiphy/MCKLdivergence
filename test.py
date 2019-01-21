#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 13 00:51:55 2019

@author: ahmadi
"""

from MCKLD import Rel_ent,Exp_rel_ent
import numpy as np
import os
cwd = os.getcwd()


RE=Rel_ent(cwd + '/REdata/chain.out',cwd + '/REdata/chainprob.out',cwd + '/REdata/lnprior.out')
re=RE.Run()
print(re)


M = np.genfromtxt(cwd+'/EREdata/M.txt')
def usr_func(theta):
     return M@theta
ERE=Exp_rel_ent(cwd+'/EREdata/D1_sample.txt',cwd+'/EREdata/C.txt',5,12)
ere=ERE.Run(usr_func)
print(ere)
