# MCKLdivergence
A python package to estimate the relative entropy between the prior and posterior from an MCMC chain.
The code also estimates the expected relative entropy from the likelihood and a sample of prior.
For more detiales see ......

The code is written for Python 3.x in linux machin.

### Installations:
To install this package into your linux machine with pip, do the following:
+ First, make sure that [MCEvidence](https://github.com/yabebalFantaye/MCEvidence) is installed.
+ To run package in parallel mode install mpi4py and openmpi in your linux machine.
+ Then in a terminal, run 
     ```
     $ git clone https://github.com/ahmadiphy/MCKLdivergence
     $ cd MCKLdivergence
     $ pip install -e .
     ```
To install this package directly with pip without clonning:

     $ pip install -e git+https://github.com/ahmadiphy/MCKLdivergence


### Example:
In the Example folder there are two simple examples for estimation of the relative entropy and the expected relative entropy 



### If you use the code, please cite the following papers:
1- ................. (Meharbi and Ahmadi (2019))                                                                                2- https://arxiv.org/abs/1704.03472 (Heavens et. al. (2017))

