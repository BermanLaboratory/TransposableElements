from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np

def PlotScree(df):
    pca = PCA(n_components=100)

    TEPCA = pca.fit(df.transpose())

    PC_values = np.arange(pca.n_components_) + 1
    plt.plot(PC_values, pca.explained_variance_ratio_, 'o-', linewidth=2, color='blue')
    plt.title('Scree Plot')
    plt.xlabel('Principal Component')
    plt.ylabel('Variance Explained')
    plt.show()

    return pca.explained_variance_ratio_
