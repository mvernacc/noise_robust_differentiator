"""Python implementation of Pavel Holoborodko's smooth noise-robust differentiators.

See http://www.holoborodko.com/pavel/numerical-methods/numerical-derivative/smooth-low-noise-differentiators/
"""

import numpy as np
from scipy.special import binom

def derivative_n2(data: np.ndarray, dt=1., filter_length=5):
    if not filter_length % 2 == 1:
        raise ValueError('Filter length must be odd.')
    M = int((filter_length - 1) / 2)
    m = int((filter_length - 3) / 2)
    result = np.full(len(data), np.nan)
    coefs = [(1 / 2**(2 * m + 1)) * (binom(2 * m, m - k + 1) - binom(2 * m, m - k - 1))
        for k in range(1, M + 1)]
    for i in range(M, len(data) - M):
        result[i] = (1 / dt) * sum([
            coefs[k - 1] * (data[i + k] - data[i - k])
            for k in range(1, M + 1)])
    return result
