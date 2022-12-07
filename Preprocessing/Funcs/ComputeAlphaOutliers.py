import json
import numpy as np

def computealpha(n):

    # computes the alpha for the threshold when looking for outliers.
    # The value of alpha depends on the size of the dataset (n).
    # The calculation up to n = 300 were computed by Hoaglin et al; Hoaglin, D.C., and Iglewicz, B.(1987)
    # Journal    of    the    American    Statistical    Association   82, 1147 - 1149%
    # for n > 300, extrapolation function is used: 0.21 * log10(n) + 1.9; computed by Kathrin Tyryshkin (Queens Universtiy, March 2018)

    #input: Samples size (n)
    # output: alpha values for outlier detection

    # Original Author (Matlab): Kathrin Tyryshkin
    # Current Author (Python): Andrew Garven

    f = open('/Users/andrewgarven/PycharmProjects/TransposableElements/Preprocessing/Funcs/PreComputeAlpha.json')
    data = json.load(f)

    if n < 5:
        alpha = 1.5
        return alpha

    elif n > 300:
        alpha = 0.21 * np.log10(n) + 1.9
        return alpha

    else:
        close = min(data.keys(), key=lambda x: abs(int(x) - n))
        alpha = data[close]
        return alpha
