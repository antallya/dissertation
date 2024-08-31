import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dissertation_test import n_values

df_proportion=pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/64bits/results.csv",
               header=None, usecols=list(range(4,19)))
dfHll = pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/64bits/HllResults.csv",
                    header=None)
dfHll.columns = range(4,19)
print(dfHll)
n_values = [5,10,100,500,750,1000]
actual_unique_entries = [5, 10, 99, 475, 696, 900]

df_proportion.index = n_values
dfHll.index = n_values
sns.set_theme()

# HLL estimates vs actual unique entries
plt.figure(figsize=(14, 8))

for i, sample_size in enumerate(dfHll.index):
    plt.plot(dfHll.columns, dfHll.loc[sample_size], marker='o', label=f'Sample Size {sample_size} HLL Estimate')
    plt.plot(dfHll.columns, [actual_unique_entries[i]] * len(dfHll.columns), '--', label=f'Actual Unique Entries (Sample Size {sample_size})')

plt.xlabel('Bit Size (p)')
plt.ylabel('Cardinality Estimate')
plt.title('HLL Estimates vs Actual Unique Entries')
plt.legend(loc='center', bbox_to_anchor=(0.9, 0.2), fontsize='small')
plt.grid(True)
plt.savefig(f'HLLvsActual.png')
plt.show()


# ALL PLOTS VS 0.5
plt.figure(figsize=(12, 8))

for i, sample_size in enumerate(df_proportion.index):
    plt.plot(df_proportion.columns, df_proportion.loc[sample_size], marker='o', label=f'Sample Size {sample_size}')

plt.axhline(y=0.5, color='teal', linestyle='--', label='Expected Proportion (0.5)')
plt.xlabel('Bit Size (p)')
plt.ylabel('Average Proportion of Zeros')
plt.title('Empirical Proportion of Zeros vs Bit Size')
plt.legend()
plt.grid(True)
plt.savefig(f'AllEmpiricalProportions.png')
plt.show()

