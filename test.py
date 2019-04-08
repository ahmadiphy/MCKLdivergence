import numpy as np
import sys
import os
cwd = os.getcwd()

from MCKLD import Rel_ent,Exp_rel_ent

#RE=Rel_ent(cwd + '/REdata/chain.out',cwd + '/REdata/chainprob.out',cwd + '/REdata/lnprior.out')
#re=RE.Run()
#print(re)
functions_path=cwd+'/Functions.py'
ERE=Exp_rel_ent(cwd+'/EREdata/D1_sample.txt',cwd+'/EREdata/C.txt',10,300)
#ere=ERE.Run()
#print(ere)
pere=ERE.PRun(2)
