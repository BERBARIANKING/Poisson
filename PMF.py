# Author:Nikolaos Bermparis
# Propability Mass Function


# Suppose you own a coffee shop, and you're interested in analyzing the number of customers that enter your shop during a certain time period.
# You want to use the Poisson distribution to model the number of customers based on historical data.


# Mean: You input the average number of customers that enter your coffee shop in an hour.
# Let's say the historical data suggests an average of 20 customers per hour.

# Range: You input a range of values, let's say from 0 to 40 customers. 
# This means you're interested in calculating probabilities for the number of customers ranging from 0 to 40.


# The program will calculate the Poisson probabilities for each value in the range based on the average of 20 customers per hour.
# The program will also display a plot showing the Poisson distribution of customer arrivals.
# The x-axis will represent the number of customers (0 to 40), and the y-axis will represent the probability of that number of customers arriving.

#Library collection
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Get user input for mean and range
mean = float(input("Enter the mean of the Poisson distribution: "))
start = int(input("Enter the start of the range (inclusive): "))
end = int(input("Enter the end of the range (inclusive): "))


# Generate range of values
#This array(k) will be used to represent the possible values of the random variable in the Poisson distribution.
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
