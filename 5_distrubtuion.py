print("LAKSHAY VERMA - DS2 - 29")
#Normal Distribution
import numpy as np                         # import for numerical operations
import matplotlib.pyplot as plt            
from scipy.stats import norm
# Generate Normal Distribution data
mu = 0
sigma = 1
data = np.random.normal(mu, sigma, 1000)

# Plot histogram data
plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')  
# bin=30 -> number of intervals
# density=true -> normalize the histogram to probability density
# alpha=0.6 -> transparency level of the histogram bars
# edgecolor='black' -> color of the histogram bin edges


xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = norm.pdf(x, mu, sigma)  # Probability density function

plt.plot(x, p, 'r', linewidth=2)  # Plot the PDF
plt.title('Normal Distribution (mean=0, std=1)')  #add title
plt.show() #display the plot

# Binomial Distribution
from scipy.stats import binom  #import binom for binomial

# Define parameters
n = 10  # number of trials
p = 0.5  # probability of success
x = np.arange(0, n+1)  #possible value 0 to n
pmf = binom.pmf(x, n, p)  # Probability mass function calculation

#plot binomial distribution
plt.bar(x, pmf, color='orange', edgecolor='black')
# bar plot of probablities
# color -> bar color
# edgecolor -> color of the bar edges

plt.title('Binomial Distribution (n=10, p=0.5)')  # add title
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.show()


#poisoon distribution 
from scipy.stats import poisson  #import poisson for poisson distribution

# define parameters
lambda_val = 4 # average rate of events (lambda)
x = np.arange(0, 15)  # possible values (0 to 14)
pmf = poisson.pmf(x,mu=lambda_val)  # Probability mass function calculation

# plot poisson distribution
plt.bar(x, pmf, color='green', edgecolor='black')
plt.title('Poisson Distribution (lambda=4)')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.show()