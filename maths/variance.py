"""
source: https://en.wikipedia.org/wiki/Variance
Variance of a discrete random variable is given by:
Var(X) = ∑((x[i] - μ)^2).P[X = x[i]]

where:
x[i]: ith possible value for X.
μ: mean or expected value of the distribution.
P[X = x[i]]: the probability mass function (PMF) that assigns a probability
to each possible value x[i]
"""


def variance_of_discrete_random_variable(values, pmf) -> float:
    """
    >>> variance_of_discrete_random_variable([1], [1.0])
    0.0
    >>> variance_of_discrete_random_variable([1, 2, 3], [0.33, 0.33, 0.33])
    0.6604
    >>> variance_of_discrete_random_variable([1000, 2000, 3000, ],[0.005, 0.005, 0.99])
    24775.0
    >>> variance_of_discrete_random_variable([1], [0.80, 0.20])
    Traceback (most recent call last):
    ...
    ValueError: Values and probabilities must be the same
    """

    if len(values) != len(pmf):
        raise ValueError("Values and probabilities must be the same")

    mean = sum(values[i] * pmf[i] for i in range(len(values)))
    squared_deviations = [(values[i] - mean) ** 2 * pmf[i] for i in range(len(values))]
    variance = sum(squared_deviations)

    return round(variance, 4)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(f"{variance_of_discrete_random_variable([1, 2, 3],[0.33, 0.33, 0.33])}")
