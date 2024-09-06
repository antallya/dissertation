import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

df=pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/64bits/results.csv",
               header=None, usecols=list(range(4,19)))

# number of hashes per experiment
n_values = [5,10,100,500,750,1000]
sns.set_theme()
xvalues=list(range(4,19))

for index, row in df.iterrows():
    # empirical distribution of proportion of zeros
    plt.figure(figsize=(12, 8))
    sns.lineplot(x=xvalues, y=row.values, color='navy', label=f'Average Proportion of Zeros (Sample Size: {n_values[index]})')
    plt.axhline(y=0.5, color='teal', linestyle='--', label='Expected Proportion (0.5)')

    # log2(n) --> max number of buckets
    log2_n = np.log2(n_values[index])
    plt.hlines(y=0.5, xmin=4, xmax=log2_n, color='orange', linestyle='--', label=f'Domain for n={n_values[index]}')
    plt.plot(log2_n, 0.5, 'ro', label=f'log2({n_values[index]}) = {log2_n:.2f}')

    plt.xticks(xvalues)
    plt.xlabel('Number of bits analysed (k)')
    plt.ylabel('Proportion of Zeros')
    plt.title(f'Average Proportion of Zeros per p bits analysed (Sample Size: {n_values[index]})')
    plt.legend()
    plt.savefig(f'empirical_proportion_{index}.png')
    plt.show()

    # deviation from 0.5
    # plt.figure(figsize=(12, 6))
    # deviation_from_05 = np.abs(row.values - 0.5)
    # sns.lineplot(x=xvalues, y=deviation_from_05, color='red', label=f'Deviation from 0.5 (Sample Size: {n_values[index]})')
    #
    # threshold = 0.01  # threshold error for small devs
    # small_deviation_indices = np.where(deviation_from_05 < threshold)[0]
    # plt.scatter(x=np.array(xvalues)[small_deviation_indices],
    #             y=deviation_from_05[small_deviation_indices], color='orange', label=f'Small Deviations (aprox: {threshold})')
    #
    # plt.xticks(xvalues)
    # plt.xlabel('Number of bits analysed (p)')
    # plt.ylabel('Deviation from 0.5')
    # plt.title(f'Deviation of Proportion of Zeros from 0.5 (Sample Size: {n_values[index]})')
    # plt.legend()
    # plt.savefig(f'deviation_{index}.png')
    # plt.show()
    #
