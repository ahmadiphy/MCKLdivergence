import sys

import numpy as np
from numpy.linalg import inv
import os
cwd = os.getcwd()
from mpi4py import MPI
import time


if __name__ == "__main__":
    sample_path = sys.argv[1]
    likeC_path = sys.argv[2]
    M_path = sys.argv[3]
    mainSRC = sys.argv[4]
    l = int(sys.argv[5])
    nn = int(sys.argv[6])
    sample = np.genfromtxt(sample_path)
    like_cov = np.genfromtxt(likeC_path)
    M = np.genfromtxt(M_path)
    ere=0




def model_fun(theta):
     return M@theta
#This function has been used in the code
def MAH_Distance(x,y):
     return np.transpose(x)@y@x

def jfun(i,l,data,sample,cov_like_inv):
     ss=0
     fl=float(l)
     for j in range(l):
          ss=ss+np.exp(-0.5*MAH_Distance(data[i]-model_fun(sample[j]),cov_like_inv))
     term2 = np.log(ss/fl)
     term1 = -0.5*MAH_Distance(data[i]-model_fun(sample[i]),cov_like_inv)
     return term1-term2

def expecte_relative_entropy(sample,likelihood_cov,fun,l,n):
     #genertaing data sample
     fl=float(l)
     cov_like_inv = inv(likelihood_cov)
     data = np.zeros((l,n))
     for i in range(l):
          data[i] = np.random.multivariate_normal(fun(sample[i]), likelihood_cov) 

     comm = MPI.COMM_WORLD
     rank = comm.Get_rank()
     size = comm.Get_size()

     a = 1
     perrank = l//size
     summ = np.zeros(1)

     comm.Barrier()
     start_time = time.time()
     temp = 0
     for k in range(a + rank*perrank, a + (rank+1)*perrank):
         temp = temp + jfun(k-1,l,data,sample,cov_like_inv)

     summ[0] = temp

     if rank == 0:
         total = np.zeros(1)
     else:
         total = None

     comm.Barrier()
     #collect the partial results and add to the total sum
     comm.Reduce(summ, total, op=MPI.SUM, root=0)

     stop_time = time.time()

     if rank == 0:
         #add the rest numbers to 1 000 000
         #for i in range(a + (size)*perrank, b+1):
         #    total[0] = total[0] + i
         print ("The res: ", total[0]/fl)
         print ("time spent with ", size, " threads in milliseconds")
         print ("-----", int((time.time()-start_time)*1000), "-----")
         exp_res=total[0]/fl
         return exp_res
expecte_relative_entropy(sample,like_cov,model_fun,nn,10) 
