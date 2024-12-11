import math
import numpy as np
from collections import Counter
from scipy.stats import chi2


class ChiSquaredTest:
    def __init__(self, sample, alpha):
        self.sample = sample
        self.alpha = alpha
        self.n = len(sample)
        self.unique_values = range(0, 21)

    def calculate_frequencies(self):
        frequencies = Counter(self.sample)
        freq_array = np.array([frequencies.get(i, 0) for i in self.unique_values])
        return freq_array

    def theoretical_normal_distribution(self):
        mean = np.mean(self.sample)
        std_dev = np.std(self.sample, ddof=1)
        probabilities = [
            self.normal_probability(i, mean, std_dev) for i in self.unique_values
        ]
        return np.array(probabilities) * self.n

    def normal_probability(self, x, mean, std_dev):
        return (
                1
                / (std_dev * math.sqrt(2 * math.pi))
                * math.exp(-0.5 * ((x - mean) / std_dev) ** 2)
        )

    def theoretical_uniform_distribution(self):
        probability = 1 / len(self.unique_values)
        return np.array([probability * self.n] * len(self.unique_values))

    def calculate_chi_squared(self, observed, expected):
        return np.sum((observed - expected) ** 2 / expected)

    def run_test(self):
        # Calculate the observed frequencies of the sample.
        observed = self.calculate_frequencies()

        # Calculate the expected frequencies for both normal and uniform distributions.
        expected_normal = self.theoretical_normal_distribution()
        expected_uniform = self.theoretical_uniform_distribution()

        # Calculate the Chi-squared statistic for both normal and uniform distributions.
        chi_squared_normal = self.calculate_chi_squared(observed, expected_normal)
        chi_squared_uniform = self.calculate_chi_squared(observed, expected_uniform)

        # Degrees of freedom is the number of unique values minus 1.
        degrees_of_freedom = len(self.unique_values) - 1

        # Calculate the critical Chi-squared value from the Chi-squared distribution (using the given significance level).
        chi_squared_critical = chi2.ppf(1 - self.alpha, degrees_of_freedom)

        # Compare the calculated Chi-squared values with the critical value to determine if the distributions match.
        is_normal = chi_squared_normal < chi_squared_critical
        is_uniform = chi_squared_uniform < chi_squared_critical

        # Return a dictionary with the test results: observed frequencies, Chi-squared values, and distribution match outcomes.
        return {
            "observed": observed,
            "chi_squared_normal": chi_squared_normal,
            "chi_squared_uniform": chi_squared_uniform,
            "chi_squared_critical": chi_squared_critical,
            "is_normal": is_normal,
            "is_uniform": is_uniform,
        }
