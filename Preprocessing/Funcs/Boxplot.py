import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def GenerateBoxplot(df, saveloc):

    # This function standardizes and normalizes '-omic' expression datasets to evaluate outliers and batch effects
    # Inputs
    # df = Ordered '-omic' pandas dataframe with samples as columns and 'genes' as rows
    # saveloc = str containing name and location of output png file
    # Outputs
    # boxplot saved as a png file

    dflog = np.log(df + 1)
    TEZeroCentred = dflog - dflog.mean()
    figure(figsize=(20, 10), dpi=250)
    plt.boxplot(TEZeroCentred, meanline=True)
    plt.title('UROMOL Transcriptomic Data (log Transformed, Zero Centered)')
    plt.ylabel('Transcriptomic Expression log2(x)')
    plt.xlabel('Ordered UROMOL samples')
    plt.xticks([])
    plt.savefig(saveloc)
    plt.show()
