import matplotlib.pyplot as plt
import numpy as np

def plotSpearman(df, genete):


    Q3 = np.quantile(df, 0.75)
    Q1 = np.quantile(df, 0.25)

    IQR = Q3 - Q1
    outlierCutoff = Q1 - (IQR * 2.2)

    plt.axhline(outlierCutoff, c='r', linestyle='--')
    plt.scatter(range(1, len(df) + 1), df)
    plt.title(f'UROMOL {genete} Transcriptomic Data Spearman assessment')
    plt.ylabel('Mean Spearmans Rank Correlation Coefficient')
    plt.xlabel('Ordered UROMOL samples')
    plt.show()