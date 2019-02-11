import numpy as np
from numpy.linalg import inv
import os
from mpi4py import MPI
import time
cwd = os.getcwd()
def expecte_relative_entropy(sample,likelihood_cov,fun,l,n):
     #genertaing data sample

     cov_like_inv = inv(likelihood_cov)
     data = np.zeros((l,n))
     for i in range(l):
          data[i] = np.random.multivariate_normal(fun(sample[i]), likelihood_cov) 
     ss=np.zeros(l)
     term2=np.zeros(l)
     term1=np.zeros(l)
     
     comm = MPI.COMM_WORLD
     rank = comm.Get_rank()
     size = comm.Get_size()
     a=1
     perrank = l//size
     summ = np.zeros(1)
     
     comm.Barrier()
     start_time = time.time()

     temp = 0
     for i in range(a + rank*perrank, a + (rank+1)*perrank):
          ss[i-1] = 0
          for j in range(l):
               ss[i-1] = ss[i-1] +  np.exp(-0.5*MAH_Distance(data[i-1]-fun(sample[j]),cov_like_inv)) 
          term2[i-1] = np.log(ss[i-1]/l)
          term1[i-1] = np.exp(-0.5*MAH_Distance(data[i-1]-fun(sample[i-1]),cov_like_inv))
          temp = temp + term1[i-1] - term2[i-1]
  
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
        print ("time spent with ", size, " threads in milliseconds")
        print ("-----", int((time.time()-start_time)*1000), "-----")
        print(total[0]/l)

if __name__ == "__main__":
    sample_path = sys.argv[1]
    likeC_path = sys.argv[2]
    mainSRC = sys.argv[3]
    l = int(sys.argv[4])
    n = int(sys.argv[5])
    sample = np.genfromtxt(sample_path)
    likelihood_cov = np.genfromtxt(likeC_path)
    expecte_relative_entropy(sample,likelihood_cov,fun,l,n)
