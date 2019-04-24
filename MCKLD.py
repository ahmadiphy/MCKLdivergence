# -*- coding: utf-8 -*-
"""
@author: Abolfazl Ahmadi
"""

__authors__ = "Ahmad Mehrabi & Abolfazl Ahmadi Rahmat"
__license__ = "MIT"
__version_info__ = ('20','April','2019')
__version__ = '-'.join(__version_info__)
__status__ = "Development"


__check_mce_installed__=False
try:
    from MCEvidence import MCEvidence
    __check_mce_installed__=True
except:
    print("Dependency ERROR! 'MCEvidence not found!")
    __check_mce_installed__=False
    
import numpy as np
import inspect, os, sys


class BaseFuncs:
    def printErr(self,info):
        print("ERROR!:{}".format(info))
    def printInfo(self,info):
        print("INFO:{}".format(info))
        # Disable
    def blockPrint(self):
    	sys.stdout = open(os.devnull, 'w')
    # Restore
    def enablePrint(self):
    	sys.stdout = sys.__stdout__
        
class Rel_ent(BaseFuncs):
    'this is mylass form of the package'
    def __init__(self,chain_path=None,lnprior_path=None,inThinlen=0.0,inBurnlen=0.0):
        self.state=False
        if chain_path!=None:
            if lnprior_path!=None:
                self.state=True
            else:
                self.printErr('Problem in loading lnprior')
        else:
            self.printErr('Problem in loading chain!')
        
        if self.state==True:
            self.Thinlen=inThinlen
            self.Burnlen=inBurnlen
            self.printInfo('Loading chain from {}'.format(chain_path))
            self.chain = np.genfromtxt(chain_path)
            self.printInfo('Loading lnprior from {}'.format(lnprior_path))
            lnprior = np.genfromtxt(lnprior_path)
            self.Blen=int(self.Burnlen*len(lnprior))
            lnp=self.chain[:,1]
            self.printInfo("All data loaded.")
            self.lnlike = lnp - lnprior
            self.lnlike=self.lnlike[self.Blen:]
    def printRes(self,resVec):
        for k in range(len(resVec)):
            print('D[k={}] = {}'.format(k+1,resVec[k]))
    def myResult(self,avgL,mce):
        result=np.zeros(len(mce))
        result=-1*mce+avgL
        return result
    def Run(self):
        if self.state==True:
            self.printInfo("Calculatong MCEvidence...")
            
            mce=MCEvidence([self.chain],ischain=True,thinlen=self.Thinlen,burnlen=self.Burnlen).evidence(pos_lnp=True)
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
    def __init__(self,sample_path=None,function_path=None,lcm=np.zeros(1),n_in=0):
        self.state=False
        if sample_path!=None:
            if len(lcm)!=1:
                self.state=True
            else:
                self.printErr('input error, Like Cov Matrix!')
        else:
            self.printErr('import error, sample path dose not exist!')
        if self.state==True:
            self.sPath=sample_path
            self.Like_Cov_Matrix=lcm
            self.n=n_in
            self.fpath=function_path[:-12]
            sys.path.append(self.fpath)
            print(self.fpath)
            from Functions import model_function
            self.mf=model_function()
    def check_input(self):
        if len(self.Like_Cov_Matrix)>self.n or len(self.Like_Cov_Matrix)!=len(self.Like_Cov_Matrix[0]):
            self.printErr('The likelihood_cov matrix should be n*n')
            self.state=False
    #This function has been used in the code
    def MAH_Distance(self,x,y):
        return np.transpose(x)@y@x
    def jfun(self,i,l,data,cov_like_inv):
        ss=0
        fl=float(l)
        for j in range(l):
            ss=ss+np.exp(-0.5*self.MAH_Distance(data[i]-self.mf.fun(self.sample[j]),cov_like_inv))
        term2 = np.log(ss/fl)
        term1 =  -0.5*self.MAH_Distance(data[i]-self.mf.fun(self.sample[i]),cov_like_inv)
        return term1-term2
    def Run(self,l_in=0):
        self.l=l_in
        if self.l==0:
    		#ERRoR
            self.state=False
        if self.state==True:
            self.printInfo('file importing...')
            self.printInfo('samples file importing '+self.sPath)
            self.sample = np.genfromtxt(self.sPath)
            self.printInfo('checking input files...')
            self.check_input()
            if self.l>len(self.sample):
                self.printErr('The number of sample used to estimate expected relative entropy should be smaller than given sample size')
                self.state=False
            if self.state==True:
                from numpy.linalg import inv
                self.printInfo('Expected Relative Entropy (ERE):')
                self.printInfo('genertaing data sample...')
                cov_like_inv = inv(self.Like_Cov_Matrix)
                data = np.zeros((self.l,self.n))
                for i in range(self.l):
                    data[i] = np.random.multivariate_normal(self.mf.fun(self.sample[i]), self.Like_Cov_Matrix) 
                exp_rel = 0
                for m in range(self.l):
                    exp_rel = exp_rel + self.jfun(m,self.l,data,cov_like_inv)
                result=(exp_rel/self.l)
                self.printInfo(result)
                return result 
        else:
            self.printErr('State Error')
    def PRun(self,l_in=0,coreN=1):
    	self.l=l_in
    	if self.l==0:
    		#ERROR
    		self.printErr("data length is zero")
    		self.state=False
    	else:
    		self.check_input()
    	import multiprocessing
    	cn=multiprocessing.cpu_count()
    	if coreN>cn:
    		self.printErr(
    			"number of threads for this machine cannot be larger than "+
    			str(cn)+
    			" (number of cores of this machine)!"
    			)
    		self.state=False
    	if self.state==True:
            lPath=self.fpath+'cov.txt'
            np.savetxt(lPath, self.Like_Cov_Matrix)
            bashCommand="mpiexec -np "+str(coreN)+" python ./parallelERE.py"
            bashCommand=bashCommand+" "+str(self.n)+" "+str(self.l)+" "+str(self.sPath)+" "+str(lPath)+" "+str(self.fpath)
            os.system(bashCommand)
            CF=self.fpath+'cash.txt'
            result=np.genfromtxt(CF)
            os.remove(CF)
            os.remove(lPath)
            return float(result)
