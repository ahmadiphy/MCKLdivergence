"""
@author: Abolfazl Ahmadi

model functions

"""

import sys
import os
cwd = os.getcwd()
import numpy as np

#do not change class name
class model_function:
	def __init__(self,a=0):
		M_path=cwd +'/M.txt'
		self.M = np.genfromtxt(M_path)
	def fun(self,theta):#do not change function name
		return self.M@theta
