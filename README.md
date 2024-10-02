# Visualizing the Tuning of Bucket Parameters in HLL

## Overview
These folders contain the visualizations generated from the analysis of the bucket parameter k tuning in the HyperLogLog (HLL) algorithm. The visualizations demonstrate the relationship between the empirical proportion of zeros in hash values and the expected binomial distribution. They also show the impact of varying $k$ on the accuracy of cardinality estimation and testing against real HLL values.

## Visualization Details

### Empirical vs Theoretical Proportion of Zeros:
- These plots compare the empirical proportion of zeros observed across different bit positions with the expected binomial distribution $X_i \sim Binomial(n, \frac{1}{2})$
- The x-axis represents different sample sizes, while the y-axis represents the proportion of zeros.
- The point where the two distributions align or almost align is where the bucket parameter $k$ is optimal.

### HLL Estimates vs Actual Unique Counts:
- These plots show the performance of the HLL algorithm for different values of $k$. The x-axis represents the number of samples, while the y-axis represents the estimated and actual cardinality.
- The goal is to find the $k$-value where the HLL estimate is closest to the actual unique count.

### Plot Descriptions
- empirical_vs_theoretical_zeros.png: Compares the empirical and theoretical proportions of zeros for different $k$ values across different sample sizes.
- hll_estimates_vs_actual.png: Shows the HLL estimates compared to actual unique counts for various bucket sizes across different sample sizes.

### Conclusion
- These visualizations help validate the proposed heuristic for selecting the optimal bucket parameter in the HLL algorithm. By aligning the empirical proportion of zeros with the theoretical binomial distribution, we ensure that hash values are uniformly distributed across buckets, optimizing both accuracy and memory efficiency.
