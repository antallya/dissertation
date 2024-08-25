import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom

df=pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/results.csv",
               header=None, usecols=list(range(0,128)))
print(df.head())
n_values = [5,10,50,100,500,750,1000]
# Setting theme
sns.set_theme()
xvalues=list(range(0,128,8))
# Function for plotting each row of the dataframe
for index, row in df.iterrows():
    # plot
    plt.figure(figsize=(8,4))
    sns.lineplot(x=row.index, y=row.values)

    # labels and axis
    plt.xticks(xvalues)
    plt.xlabel('Number of bytes (8 bits) analysed')
    plt.ylabel('Probability')
    plt.title('Probability of getting a zero per bit space analysed')
    plt.legend()

    # display
    plt.show()

#sns.relplot(data=df, x="probabilities", y="")

