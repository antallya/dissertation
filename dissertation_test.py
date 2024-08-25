import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

df=pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/results.csv",
               header=None, usecols=list(range(0,32)))
print(df.head())
n_values = [5,10,50,100,500,750,1000]
# Setting theme
sns.set_theme()
xvalues=list(range(0,32,8))
# Function for plotting each row of the dataframe
for index, row in df.iterrows():
    # plot
    plt.figure(figsize=(8,4))
    sns.lineplot(x=row.index, y=row.values)

    # binomial distribution
    for i, column in enumerate(row.index):
        n = n_values[index]  # Use corresponding n value based on row index
        p = 1 / (2**i)  # Probability for the binomial distribution
        binom_value = binom.pmf(k=int(n*p), n=n, p=p)

        # Plot the binomial point
        plt.scatter(column, binom_value, color='red', label=f'Binom (n={n}, p=1/2^k)' if i == 0 else "")
        
    # labels and axis
    plt.xticks(xvalues)
    plt.xlabel('Number of bytes (8 bits) analysed')
    plt.ylabel('Probability')
    plt.title('Probability of getting a zero per bit space analysed')
    plt.legend()

    # display
    plt.show()

#sns.relplot(data=df, x="probabilities", y="")



