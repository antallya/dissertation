import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

df=pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/results.csv",
               header=None, usecols=list(range(0,32)))
print(df.head())
# number of hashes per experiment
n_values = [5,10,50,100,500,750,1000]
# set theme
sns.set_theme()
xvalues=list(range(0,32, 2))
# plotting each row of the dataFrame
for index, row in df.iterrows():
    # plot
    plt.figure(figsize=(8,6))
    sns.lineplot(x=row.index, y=row.values, color='navy')

    # binomial distribution
    for i, column in enumerate(row.index):
        if i == 0:
            continue # skip the analysis of 0 bit position because the probability =1

        n = n_values[index]  # n value corresponding to row index
        p = 1 / (2**i)  # binomial distribution probability
        binom_value = binom.pmf(k=int(n*p), n=n, p=p) #binomial distn means!!!

        # scatter plot for the binomial sigmoid
        plt.scatter(column, binom_value, color='teal', label=f'Binom (n={n}, p=1/2^k)' if i == 0 else "")

    # labels and axis
    plt.xticks(xvalues)
    plt.xlabel('Number of bits analysed')
    plt.ylabel('Probability')
    plt.title('Probability of getting a zero per bit space analysed')
    plt.legend()

    # display
    plt.show()




