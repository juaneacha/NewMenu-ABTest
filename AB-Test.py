

#Code for Mann-Whitney U test 
from statistics import median
from scipy.stats import mannwhitneyu
import scipy.stats as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


#Load data
df = pd.read_csv('Wages from Ala Restaurant (05_09_2024 - 01_30_2025) - Sheet1.csv')
print(df)

#Sampling the data for old and new menus
df = df[:12]
df['Gross Earnings'] = df['Gross Earnings'].astype(float)
oldMenu = df[df['Menu'] == 'Old']['Gross Earnings']
newMenu = df[df['Menu'] == 'New']['Gross Earnings']

#Show data for old and new menus
print(oldMenu)
print(newMenu)

#Perform mann whitney test 
stat, p_val = mannwhitneyu(newMenu, oldMenu, alternative='less') 
print('Statistics=%.2f, p=%.2f' % (stat, p_val)) 

#Level of significance 
alpha = 0.05

#Conclusion 
#Introducing a New Menu can increase revenue by 10% to 15% according to Sling. Therefore:
    #The null hypothesis is that new menu's revenue is GREATER than old menu's revenue
    #The alternate hypothesis is that new menu's revenue is LESS than old menu's revenue

if p_val < alpha: 
    print('Reject Null Hypothesis (new menu`s revenue IS NOT greater than old menu`s)') 
else: 
    print('Do Not Reject Null Hypothesis (new menu`s revenue IS greater than old menu`s)')




#Two Sample Mean Non-Parametric 95% Confidence Interval


#Declare Dataset and Confidence Interval
twoSampleDataset = list() 
confidence = 0.95

#Generate 10,000 random samples means from both menu datasets, take their difference, and store in twoSampleDataset
for i in range(10000): 
    oldMenuSample = np.random.choice(oldMenu, size = len(oldMenu))
    newMenuSample = np.random.choice(newMenu, size = len(newMenu))

    oldMenuXbar = np.mean(oldMenuSample)
    newMenuXbar = np.mean(newMenuSample)

    twoSampleDataset.append(newMenuXbar - oldMenuXbar)

#Calculate Statistical Parameters
mean = np.mean(twoSampleDataset) 
standard_error_of_mean = st.sem(twoSampleDataset)
degrees_of_freedom = len(twoSampleDataset) - 1
t_critical = st.t.ppf((1 + confidence) / 2, degrees_of_freedom)
margin_of_error = t_critical * standard_error_of_mean

#Calculate Lower and Upper Bound for 95% Confidence Interval
lower_bound = mean - margin_of_error  
upper_bound = mean + margin_of_error

#Show actual mean and confidence interval
avg = np.mean(newMenu) - np.mean(oldMenu) 
print("Avg Bi-Weekly Loss: " + str(avg))
print("95% Confidence Interval: " + str(lower_bound) + " - " + str(upper_bound))




#Simulation
sampleSize = 5
oldMenuSim = list()
newMenuSim = list()
sampleSizeList = list()
pValList = list()

#Simulate P-Value across different random samples up to a 500
while sampleSize <= 500:
    oldMenuSim = np.random.choice(oldMenu, size = sampleSize)
    newMenuSim = np.random.choice(newMenu, size = sampleSize)

    stat, p_val = mannwhitneyu(newMenuSim, oldMenuSim, alternative='less')
    sampleSizeList.append(sampleSize)
    pValList.append(p_val)

    sampleSize += 5

pValSim = pd.DataFrame({'Sample Size':sampleSizeList, 'P-Value':pValList})

x = pValSim['Sample Size']
y = pValSim['P-Value']

plt.plot(x, y, linestyle='--', marker='o', color='green', linewidth=1)
plt.xlabel("Sample Size")
plt.ylabel("P-Value")
plt.title("P-Value Simulated")
plt.grid(True)
plt.show()

print(pValSim)
