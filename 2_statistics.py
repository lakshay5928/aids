#Experiment 2: Calculate Desrcptive Statsistics for a dataset
#Objective: to compute mean ,mode , median .standard deivation,skewness and kurtosis using python
data = [122, 115, 125, 182, 139, 812, 516, 144, 413, 124, 197, 158, 319, 720, 121]
n = len(data)
# 1. Mean
mean = sum(data) / n   
# 2. Mode
frequency = {}   
for item in data:
    frequency[item] = frequency.get(item, 0) + 1
mode = max(frequency, key=frequency.get)
# 3. Median
sorted_data = sorted(data)  
if n % 2 == 0:
    median = (sorted_data[n//2 - 1] + sorted_data[n//2]) / 2
else:
    median = sorted_data[n//2]
# 4. Standard Deviation
variance = sum((x - mean) ** 2 for x in data) / (n - 1) 
std_dev = variance ** 0.5
# 5. Skewness 
skewness = sum(((x - mean)/std_dev) ** 3 for x in data) / n
# 6. Kurtosis
kurtosis = (sum(((x - mean)/std_dev) ** 4 for x in data) / n) - 3

print(f"Mean: {mean}")
print(f"Mode: {mode}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_dev}")
print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")
