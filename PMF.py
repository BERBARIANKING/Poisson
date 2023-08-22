#Author:Nikolaos Bermparis
#Propability Mass Function

#Library collection
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Get user input for mean and range
mean = float(input("Enter the mean of the Poisson distribution: "))
start = int(input("Enter the start of the range (inclusive): "))
end = int(input("Enter the end of the range (inclusive): "))

# Generate range of values
k = np.arange(start, end+1)

# Calculate Poisson probabilities
pmf = poisson.pmf(k, mu=mean)
pmf = np.round(pmf, 5)

# Print calculated probabilities
for val, prob in zip(k, pmf):
    print(f"k-value {val} has probability = {prob}")

# Plot the distribution
plt.plot(k, pmf, marker='o')
plt.xlabel('k')
plt.ylabel('Probability')
plt.title(f"Poisson Distribution (Mean = {mean})")
plt.show()
