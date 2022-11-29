import matplotlib.pyplot as plt

def TEGenomicLocationPercent(TEdf, INTRONdf, INTERGENICdf, EXONdf, cohortname):
    # sum TE expression by sample
    INTRONsum = INTRONdf.sum(axis='rows')
    INTERGENICsum = INTERGENICdf.sum(axis='rows')
    EXONsum = EXONdf.sum(axis='rows')
    TEsum = TEdf.sum(axis='rows')

    # compute the percentage of intronic TEs
    INTRONpercent = (INTRONsum / TEsum) * 100
    INTRONpercentmean = INTRONpercent.mean()
    INTERGENICpercent = (INTERGENICsum / TEsum) * 100
    INTERGENICpercentmean = INTERGENICpercent.mean()
    EXONpercent = (EXONsum / TEsum) * 100
    EXONpercentmean = EXONpercent.mean()

    # stackplot of percentage of intronic reads in transcriptomic data
    plt.stackplot(range(TEsum.shape[0]), INTRONpercent, alpha=0.33, labels=('intronic',), colors='r')
    plt.stackplot(range(TEsum.shape[0]), INTERGENICpercent, alpha=0.33, labels=('intergenic',), colors='g')
    plt.stackplot(range(TEsum.shape[0]), EXONpercent, alpha=0.33, labels=('exonic',), colors='b')
    plt.axhline(INTRONpercentmean, linestyle='--', c='r')
    plt.axhline(INTERGENICpercentmean, linestyle='--', c='g')
    plt.axhline(EXONpercentmean, linestyle='--', c='b')
    plt.xlabel(f'{cohortname} sample (ordered by ID)')
    plt.ylabel('Percentage of TEs')
    plt.title(f'Percentage of {cohortname} TE transcripts stratified by relative genomic location')
    plt.legend(loc='best')
    plt.show()