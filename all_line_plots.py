import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

df = pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/64bits/results.csv",
                 header=None, usecols=list(range(4,19)))
# number of hashes per experiment
n_values = [5, 10, 100, 500, 750, 1000]
# temporarily adding n to df
df['n'] = n_values

sns.set_theme()
xvalues = list(range(4, 19))

plt.figure(figsize=(12,8))
for index, row in df.iterrows():
    sns.lineplot(x=xvalues, y=row.drop('n').values, label=f'n = {row["n"]}')

plt.xticks(list(range(4, 19)))
plt.xlabel('Number of bits analysed')
plt.ylabel('Probability')
plt.title('Probability of getting a zero per bit space analysed')
plt.legend(title='Number of Hashes')

plt.show()

