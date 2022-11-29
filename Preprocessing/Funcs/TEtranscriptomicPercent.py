import matplotlib.pyplot as plt
import pandas as pd

def plotTEpercent(TEdf, Genedf, cohortname):

    # sum TE expression by sample
    TEsum = TEdf.sum(axis='rows')
    Genesum = Genedf.sum(axis='rows')

    # compute the total mapped transcripts
    TotalRNA = TEsum + Genesum

    # compute the percentage of TE mappings of all transcripts
    TEpercent = (TEsum / TotalRNA) * 100
    TEpercentmean = TEpercent.mean()

    # stackplot of percentage of TEs in transcriptomic data
    plt.stackplot(range(TEsum.shape[0]), TEpercent)
    plt.axhline(TEpercentmean, linestyle='--', c='r')
    plt.xlabel(f'{cohortname} sample (ordered by ID)')
    plt.ylabel('Percentage of TEs in transcriptomic data')
    plt.title(f'Percentage of TE transcripts in {cohortname} RNA-seq')
    plt.show()