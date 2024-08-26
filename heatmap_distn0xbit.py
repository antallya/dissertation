import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

df = pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/results.csv",
                 header=None, usecols=list(range(0,16)))
# number of hashes per experiment
n_values = [5, 10, 100, 500, 750, 1000]

sns.set_theme()
plt.figure(figsize=(12, 8))
ax = sns.heatmap(
    df,
    cmap='YlGnBu',
    annot=True,
    fmt='.2f',
    cbar_kws={'label': 'Proportion of Zeros'},
    linewidths=0.5,
    linecolor='gray',
    yticklabels=n_values
)

ax.set_xlabel('Bit Positions (i) analysed')
ax.set_ylabel('Sample size of hashes')
ax.set_title('Distribution of Zeros Across Multiple Bit Positions')

plt.show()