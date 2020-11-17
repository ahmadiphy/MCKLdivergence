import numpy as np
import sys
import os
cwd = os.getcwd()

from MCKLD import Exp_rel_ent



functions_path = cwd + '/Functions.py'
cov_Matrix = np.genfromtxt(cwd+'/C.txt')

ERE = Exp_rel_ent(cwd+'/D1_sample.txt', cwd+'/Functions.py', cov_Matrix, 10)
ere = ERE.Run(1000)
print('Expected relative entropy is:', ere)

#Using paralle computation 
pere = ERE.PRun(1000, 3)
print('Expected relative entropy is:', pere)
