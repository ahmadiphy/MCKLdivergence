import numpy as np
import sys
import os
cwd = os.getcwd()

from MCKLD import Rel_ent,Exp_rel_ent

RE=Rel_ent(cwd + '/REdata/chain.out',cwd + '/REdata/chainprob.out',cwd + '/REdata/lnprior.out')
re=RE.Run()
print(re)

M_path=cwd + '/M.txt'
def model_fun(theta):
     M = np.genfromtxt(M_path)
     return M@theta

ERE=Exp_rel_ent(cwd+'/EREdata/D1_sample.txt',cwd+'/EREdata/C.txt',1000,10)
ere=ERE.Run(model_fun)
print(ere)
