import numpy as np

temperature = np.array([28, 32, 31, 29, 34, 30, 33])

average = np.mean(temperature)
highest = np.max(temperature)
lowest = np.min(temperature)
above_30 = temperature[temperature > 30]
updated_temperature = temperature + 2

print("Temperatures:", temperature)
print("Average Temperature:", average)
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)
print("Temperatures above 30°C:", above_30)
print("Updated Temperatures:", updated_temperature)