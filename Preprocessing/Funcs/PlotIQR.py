import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Preprocessing.Funcs.ComputeAlphaOutliers import computealpha


def plotiqr(df, genete):

    iqr = []

    for sample in df.columns.tolist():

        Q3 = np.quantile(df.loc[:, sample], 0.75)
        Q1 = np.quantile(df.loc[:, sample], 0.25)
        IQR = Q3 - Q1
        iqr.append(IQR)

    IQR = pd.DataFrame(iqr, index=df.columns.tolist())
    Q3 = np.quantile(IQR, 0.75)
    Q1 = np.quantile(IQR, 0.25)
    IQRoutlier = Q3 - Q1
    highoutlierCutoff = Q3 + (IQRoutlier * computealpha(df.shape[1]))
    lowoutlierCutoff = Q1 - (IQRoutlier * computealpha(df.shape[1]))

    plt.axhline(highoutlierCutoff, c='r', linestyle='--')
    plt.axhline(lowoutlierCutoff, c='r', linestyle='--')
    plt.scatter(range(1, len(iqr) + 1), iqr)
    plt.title(f'UROMOL {genete} Transcriptomic Data IQR assessment')
    plt.ylabel('Inter-Quartile Range')
    plt.xlabel('Ordered UROMOL samples')

    plt.show()

    outlierdf = IQR[IQR > highoutlierCutoff].dropna() + IQR[IQR < lowoutlierCutoff].dropna()

    return outlierdf.index.values.tolist()
