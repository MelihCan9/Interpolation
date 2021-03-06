# Interpolation
Interpolation Algorithms with Covid-19 data-sets from Ministry of Health of Turkey.

### Direct Method Interpolation 
I used scipy lib to get the result faster. And the direct method interpolation method gets 3 parameters as the x points and and the y 
value corresponding to x and the data_point that we want to interpolate. After executing the method, I plotted the results like;

![image](https://user-images.githubusercontent.com/73959073/175189056-f1b40aa6-62f4-43cc-9037-b4c004e92fd2.png)


### Lagrange Interpolation 
Here in this method I am interpolating with the lagrange method, this method also gets the same parameters as direct method but 
here I did not use a built-in function because implementing the lagrange formula is easier to implementing the direct method formula in python. And finally, I again 
plotted the results like:

![image](https://user-images.githubusercontent.com/73959073/175189072-f7fdd2d5-f72c-4950-9901-a69452f46ebd.png)


### NDDP Interpolation
To be honest this method was the hardest method to implement and I got some help from lecture notes of course. Also I would like to mention that I am using an another 
method in this method called get_coeff() to get coefficients. And also finally I plotted the results of this method:

![image](https://user-images.githubusercontent.com/73959073/175189101-0207452b-14da-4d4a-bdc2-06568c4c8bd2.png)


### To compare the methods:
The Lagrange and the NDDP methods are getting the same result always as we know. And here I got the same results from these two methods as well but the direct method is 
a linear graph so the direct method gets the worst approximate results within these three methods. 
