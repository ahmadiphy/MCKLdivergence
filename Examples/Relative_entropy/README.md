# LINEAR GAUSSIAN MODEL

Assume a simple model function as:

 $ F(\Theta) = M\Theta $ 

where $$M=X^j(x_i)$$ and $$X(x)$$s are some arbitrary base functions.  
In this example we assume $X(x) = [1,x,x^2]$ base functions for a 3D problem.  
Now we choose 10 arbitrary points in range $[-5,5]$ and set $\Theta_{true} = [1,3,5]$ so we have a 10 by 3 matrix M.
Considering \sigma_i^2 = 0.8, we can simulate a data point from D = M \Theta + Gaussain_error(mean=0,cov=inv(sigma_i^2)).

Now we construct a Guassian likelihood from this data and assume following prior:  
mean_prior = [2.1,3.9,4.2]  
cov_prior = [[0.05,0.02,0.02],[0.02,0.05,0.02],[0.02,0.02,0.05]]  
The exact realtive entropy in this case is RE = 15.80  
To estimate the relative entropy from the chain, We use an MCMC sampler to generate a sample chain and compute \log(prior) at each sample.  
In example.py code, these inputs are used to estimate the relative entropy. 
Note that, we also provide M, C and D matrix for this example.  
C = likelihood covarince matrix  
D = simulated data


