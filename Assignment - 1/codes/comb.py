from scipy.stats import binom
n,p = 4, 0.5
print(f'The PMF of the binomial distribution for X=4 is: {binom.pmf(4,n,p)}')

