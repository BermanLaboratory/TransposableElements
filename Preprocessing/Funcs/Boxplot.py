import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

def GenerateBoxplot(df, genete, saveloc):

    # This function standardizes and normalizes '-omic' expression datasets to evaluate outliers and batch effects
    # Inputs
    # df = Ordered '-omic' pandas dataframe with samples as columns and 'genes' as rows
    # saveloc = str containing name and location of output png file
    # Outputs
    # boxplot saved as a png file

    zeroc = np.subtract(np.transpose(df), df.mean(axis=1))
    figure(figsize=(20, 10), dpi=250)
    plt.boxplot(zeroc, meanline=True)
    plt.title(f'UROMOL {genete} Transcriptomic Data (log Transformed, Zero Centered)')
    plt.ylabel('Transcriptomic Expression log2(x)')
    plt.xlabel('Ordered UROMOL samples')
    plt.xticks([])
    plt.savefig(saveloc)
    plt.show()
