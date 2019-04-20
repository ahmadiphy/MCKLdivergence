import numpy as np
import sys
import os
cwd = os.getcwd()
import tarfile

from MCKLD import Rel_ent,Exp_rel_ent

tf1 = tarfile.open(cwd+'REdata.tar.xz')
tf1.extractall()
RE=Rel_ent(cwd + '/REdata/chain.out',cwd + '/REdata/lnprior.out',False,4.0,0.01)
re=RE.Run()
print(re)


tf2 = tarfile.open(cwd+'EREdata.tar.xz')
tf2.extractall()
functions_path=cwd+'/Functions.py'
ERE=Exp_rel_ent(cwd+'/EREdata/D1_sample.txt',cwd+'/EREdata/C.txt',cwd+'/Functions.py',10)
ere=ERE.Run(300)
print('ere is:')
print(ere)
#pere=ERE.PRun(2,300)
