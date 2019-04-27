# LINEAR GAUSSIAN MODEL for estimation the expected relative entropy:

Here is a simple example to show how use MCKLD to estimate the expected relative entropy:
To estimate the expected relative entropy, we need a sample of D1 data and the likelihood of D2 data.  
Assume D1 is a normal Gaussian with  
cov_D1 = [[0.05,0.02,0.02],[0.02,0.05,0.02],[0.02,0.02,0.05]]  
mean_D1 = [2.1,3.9,4.2]  
In D1_sample.txt, we generate 8000 random samples from this distribution.  
Now given the D1 sample and the covarince matrix (\Sigma) of the D2 likelihood, the code estimtes the expected relative entropy.
Note that, we assume a normal likelihood for D2 N(mean=F(\Theta),cov=\Sigma).  
Where F(\Theta) is the model function which should be given by user.  
The model function must be given in Functions.py module. 

Considering above distribution for D1 and C.txt us the D2 likelihood covarinace, the exact result is 3.41  

To run the code in normol mode use:    
ERE=Exp_rel_ent('D1_sample.txt','/Functions.py',Likelihood covariance matrix,n=data dimentions)  
ere=ERE.Run(l=number of sample used to estimate the expected relative entropy)  

and in parall mode:  
ERE=Exp_rel_ent('/D1_sample.txt','/Functions.py',Likelihood covariance matrix,n=data dimentions)  
pere=ERE.PRun(l=number of sample used to estimate the expected relative entropy,number of thread)  
### Important points:
1- Do not change names in Functions.py  
2- Given model function should return an array of n dimentions.

