#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Abolfazl Ahmadi
"""

__authors__ = "Ahmad Mehrabi & Abolfazl Ahmadi Rahmat"
__license__ = "MIT"
__version_info__ = ('7','2','2019')
__version__ = '-'.join(__version_info__)
__status__ = "Development"


__check_mce_installed__=0
try:
    from MCEvidence import MCEvidence
    __check_mce_installed__=True
except:
    print("Dependency ERROR! 'MCEvidence not found!'")
    __check_mce_installed__=False
    
import numpy as np

class BaseFuncs:
    def printErr(self,info):
        print("ERROR!:{}".format(info))
    def printInfo(self,info):
        print("INFO:{}".format(info))
        
class Rel_ent(BaseFuncs):
    'this is mylass form of the package'
    def __init__(self,chain_path=None,lnp_path=None,lnprior_path=None,weight_path=None):
        self.state=False
        if chain_path!=None:
            if lnp_path!=None:
                if lnprior_path!=None:
                    self.state=True
                else:
                    self.printErr('Problem in loading lnprior')
            else:
                self.printErr('Problem in loading lnp')
        else:
            self.printErr('Problem in loading chain!')
        
        if(self.state==True):
            self.printInfo('Loading chain from {}'.format(chain_path))
            theta = np.genfromtxt(chain_path)
            self.printInfo('Loading lnp from {}'.format(lnp_path))
            lnp = np.genfromtxt(lnp_path)
            self.printInfo('Loading lnprior from {}'.format(lnprior_path))
            lnprior = np.genfromtxt(lnprior_path)
            if weight_path!=None:
                self.printInfo('Loading weight from {}'.format(weight_path))
                weight = np.genfromtxt(weight_path)
            else:
                self.printInfo('Weights had not given. So, it is a vector of ones with size of len(lnp).')
                self.printInfo('Generating the weights...')
                weight=np.ones(len(theta))
            self.printInfo("All data loaded.")
            self.printInfo('Building the chain...')
            self.chain=np.c_[weight,-lnp,theta]
            self.lnlike = lnp - lnprior
    def printRes(self,resVec):
        for k in range(len(resVec)):
            print('D[k={}] = {}'.format(k+1,resVec[k]))
    def myResult(self,avgL,mce):
        result=np.zeros(4)
        result=-1*mce+avgL
        return result
    def Run(self):
        if self.state==True:
            self.printInfo("Calculatong MCEvidence...")
            mce=MCEvidence([self.chain],ischain=True).evidence()
            avgL=np.mean(self.lnlike)
            Gresult=self.myResult(avgL,mce)
            self.printInfo("Results are :")
            self.printRes(Gresult)
            return Gresult
        else:
            self.printErr("path error!")
            return 0
class Exp_rel_ent(BaseFuncs):
    'this is expecte_relative_entropy form of the package'
    def __init__(self,sample_path=None,likeC_path=None,l_in=0,n_in=0):
        self.state=False
        if sample_path!=None:
            if likeC_path!=None:
                self.state=True
            else:
                self.printErr('input file likeC_path error')
        else:
            self.printErr('input file sample_path error')
        if self.state==True:
            self.printInfo('file importing...')
            self.sample = np.genfromtxt(sample_path)
            self.like_cov = np.genfromtxt(likeC_path)
            self.l=l_in
            self.n=n_in
        if len(self.like_cov)!=self.n and len(self.like_cov[0])!=self.n:
            self.printErr('The likelihood_cov matrix should be n by n')
            self.state=False
        if l_in>len(self.sample):
            self.printErr('The number of sample used to estimate expected relative entropy should be smaller than given sample size')
            self.state=False
    #This function has been used in the code
    def MAH_Distance(self,x,y):
        return np.transpose(x)@y@x
    def Run(self,fun):
        if self.state==True:
            from numpy.linalg import inv
            self.printInfo('Expecte Relative Entropy (ERE):')
            self.printInfo('genertaing data sample...')
            cov_like_inv = inv(self.like_cov)
            data = np.zeros((self.l,self.n))
            for i in range(self.l):
                data[i] = np.random.multivariate_normal(fun(self.sample[i]),self.like_cov) 
            exp_rel = 0
            for i in range(self.l):
                ss = 0
                for j in range(self.l):
                    ss = ss +  np.exp(-0.5*self.MAH_Distance(data[i]-fun(self.sample[j]),cov_like_inv)) 
                term2 = np.log(ss/self.l)
                term1 = np.exp(-0.5*self.MAH_Distance(data[i]-fun(self.sample[i]),cov_like_inv))
                exp_rel = exp_rel + term1 - term2
            result=exp_rel/self.l
            self.printInfo('ERE = '+str(result))
            return result
        else:
            self.printErr('State Error')
class PExp_rel_ent(BaseFuncs):
    'run parallel function parallelERE.py by passing input functions'
    def __init__(self,sample_path=None,likeC_path=None,l_in=0,n_in=0,):
        self.state=False
        if sample_path!=None:
            if likeC_path!=None:
                self.state=True
            else:
                self.printErr('input file likeC_path error')
        else:
            self.printErr('input file sample_path error')
        if self.state==True:
            self.sPath=sample_path
            self.lPath=likeC_path
            
    def run(self,coreN):
        bashCommand="mpirun -np "str(coreN)" python ./parallelERE.py"
        bashCommand=bashCommand+" "+str(self.sPath)+" "+str(self.lPath)+" "
        import subprocess
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output, error = process.communicate()
        outSTR=str(output)
        print(outSTR[2:-3])
        if error!=None:
            print(error)
