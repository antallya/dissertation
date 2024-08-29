import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binom, chi2

df=pd.read_csv("/home/antalya/CLionProjects/AntalyasGuesser/sampleFiles/64bits/results.csv",
               header=None, usecols=list(range(0,32)))
print(df.head())
# number of hashes per experiment
n_values = [5,10,100,500,750,1000]
# set theme
sns.set_theme()
xvalues=list(range(0,32, 2))

# dictionary with the results for each sample size (n)
results = {}

for n in n_values:
    expected_counts = {}
    chi_square_stats = {}
    p_values = {}

    for i in df.columns:
        p = 1 / (2 ** i)
        # expected counts for each bit position i
        expected = binom.mean(n, p)
        expected_counts[i] = expected / n # normalised by n to compare with proportions

        # observed counts
        observed = df[i].values * n  # counts for current n

        # chi-square statistic
        chi_square = ((observed - expected) ** 2 / expected).sum()
        chi_square_stats[i] = chi_square

        # p-value
        df_degrees_of_freedom = len(df) - 1  # Degrees of freedom (n-1)
        p_value = chi2.sf(chi_square_stats[i], df_degrees_of_freedom)
        p_values[i] = p_value

    # Store the results for this n
    results[n] = {
        'Expected Counts': expected_counts,
        'Chi-Square Statistic': chi_square_stats,
        'p-Value': p_values
    }

    compiled_results = []

    for n, res in results.items():
        for i in df.columns:
            compiled_results.append({
                'Sample Size (n)': n,
                'Bit Position (i)': i,
                'Chi-Square Statistic': res['Chi-Square Statistic'][i],
                'p-Value': res['p-Value'][i]
            })

    results_df = pd.DataFrame(compiled_results)

    print(results_df)

# Chi-Square Statistic vs. Bit Position for different sample sizes
sns.lineplot(data=results_df, x='Bit Position (i)', y='Chi-Square Statistic', hue='Sample Size (n)')
plt.title('Chi-Square Statistic vs. Bit Position for Different Sample Sizes')
plt.show()

# p-Value vs. Bit Position for different sample sizes
sns.lineplot(data=results_df, x='Bit Position (i)', y='p-Value', hue='Sample Size (n)')
plt.axhline(0.05, color='red', linestyle='--')  # Significance level
plt.title('p-Value vs. Bit Position for Different Sample Sizes')
plt.show()