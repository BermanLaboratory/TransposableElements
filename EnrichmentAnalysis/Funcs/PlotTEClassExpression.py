import matplotlib.pyplot as plt
import numpy as np

def plotClassExp(TEdf, cohortname):

    TEdf = np.log10(TEdf.sort_values('LINE'))

    plt.clf()
    plot1, = plt.plot(range(TEdf.shape[0]), TEdf.iloc[:,0], alpha=1, )
    plot2, = plt.plot(range(TEdf.shape[0]), TEdf.iloc[:, 1], alpha=1)
    plot3, = plt.plot(range(TEdf.shape[0]), TEdf.iloc[:, 2], alpha=1)
    plot4, = plt.plot(range(TEdf.shape[0]), TEdf.iloc[:, 3], alpha=1)
    plot5, = plt.plot(range(TEdf.shape[0]), TEdf.iloc[:, 4], alpha=1)
    plt.xlabel(f'{cohortname} sample - Ordered by ascending LINE expression')
    plt.ylabel('VST Standardized Transcriptomic Expression (log10)')
    plt.title(f'Percentage of TEs Stratified by Class - Ordered by LINE Expression ({cohortname})')
    plt.legend([plot1, plot2, plot3, plot4, plot5], ["LINE", "SINE", 'LTR', 'DNA', 'Retroposon'])
    plt.show()
