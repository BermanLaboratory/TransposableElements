import matplotlib.pyplot as plt
import numpy as np

def plotSpearman(df):


    Q3 = np.quantile(df, 0.75)
    Q1 = np.quantile(df, 0.25)

    IQR = Q3 - Q1
    outlierCutoff = Q1 - (IQR * 1.5)

    plt.axhline(outlierCutoff, c='r', linestyle='--')
    plt.scatter(range(1, len(df) + 1), df)
    plt.show()