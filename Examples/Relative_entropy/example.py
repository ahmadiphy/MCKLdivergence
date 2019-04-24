import numpy as np
import sys
import os
cwd = os.getcwd()

from MCKLD import Rel_ent,Exp_rel_ent


RE=Rel_ent(cwd + '/chain.txt',cwd + '/lnprior.txt',0.0,0.0)
re=RE.Run()
print(re)


