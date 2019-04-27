# LINEAR GAUSSIAN MODEL for estimation the expected relative entropy:

Here is a simple example to show how use MCKLD to estimate the expected relative entropy:
To estimate the expected relative entropy, we need a sample of D_1 data and the likelihood of D_2 data.  
Assume D_1 is a normal Guassian with  
cov_D_1 = [[0.05,0.02,0.02],[0.02,0.05,0.02],[0.02,0.02,0.05]]  
mean_D_1 = [2.1,3.9,4.2]  
In D1_sample.txt, we generate 8000 random samples from this distribution.  
Now given the D_1 sample and the covarince matrix (\Sigma) of the D_2 likelihood, the code estimtes the expected relative entropy.
Note that, we assume a normal likelihood for D_2 N(mean=F(\Theta),cov=\Sigma).  
Where F(\Theta) is the model function which should be given by user.  
The model function must be given in Functions.py module.  
To run the code in normol mode use:  
ERE=Exp_rel_ent(cwd+'/D1_sample.txt',cwd+'/Functions.py',cov_Matrix,n=data dimentions)  
ere=ERE.Run(l=number of sample used to estimate the expected relative entropy)  

and in parall mode:
ERE=Exp_rel_ent(cwd+'/D1_sample.txt',cwd+'/Functions.py',cov_Matrix,n=data dimentions)  
pere=ERE.PRun(l=number of sample used to estimate the expected relative entropy,number of thread)  
### Important points:
1- Do not change names in Functions.py  
2- Given model function should return an array of n dimentions.

