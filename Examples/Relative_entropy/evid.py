from MCEvidence import MCEvidence
import numpy as np
import math
import time
import os
cwd = os.getcwd()



mce=MCEvidence(cwd + '/chain.txt',ischain=True,thinlen=0.0,burnlen=0.,kmax= 5).evidence(pos_lnp=True)
