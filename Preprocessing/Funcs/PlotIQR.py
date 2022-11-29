import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


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
    outlierCutoff = Q3 + (IQRoutlier * 2.2)

    plt.axhline(outlierCutoff, c='r', linestyle='--')
    plt.scatter(range(1, len(iqr) + 1), iqr)
    plt.title(f'UROMOL {genete} Transcriptomic Data IQR assessment')
    plt.ylabel('Inter-Quartile Range')
    plt.xlabel('Ordered UROMOL samples')

    plt.show()

    return IQR[IQR > outlierCutoff].dropna()
