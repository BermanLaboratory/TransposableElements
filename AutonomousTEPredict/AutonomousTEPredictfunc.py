import pandas as pd
import pyensembl
import pybedtools
import scipy.stats as stats

def AutonomousTEPredict(TransposableElement, Gene, Locality):

    Gene.index = [x.split('.')[0] for x in Gene.index.values.tolist()]
    data = pyensembl.EnsemblRelease(77)

    elementLocations = []

    for i, element in enumerate(TransposableElement.index.values.tolist()):
        if '_' in element:
            components = element.split(',')[0].split('_')
            if len(components) < 6:
                continue
            else:
                chromosome = 'chr' + str(components[2])
                start = components[4]
                end = components[5]
                if start == '' or end == '':
                    continue
                else:
                    elementLocation = [chromosome, int(start) - Locality, int(end) + Locality, element]
                    elementLocations.append(elementLocation)
        else:
            print('please review elements string format')

    geneLocations = []

    try:
        for i, ensembl in enumerate(Gene.index.values.tolist()):
            chromosome = 'chr' + str(data.gene_by_id(ensembl).contig)
            start = str(data.gene_by_id(ensembl).start)
            end = str(data.gene_by_id(ensembl).end)
            gene = str(data.gene_by_id(ensembl).gene_name)
            geneLocation = [chromosome, int(start), int(end), gene]
            geneLocations.append(geneLocation)
    except ValueError:
        pass

    TE = pybedtools.BedTool(elementLocations)
    GENE = pybedtools.BedTool(geneLocations)

    intersect = TE.intersect(GENE, wo=True)
    intersectdf = pd.read_table(intersect.fn,
                                names=['TEchr', 'TEstart', 'TEend', 'TEname', 'GENEchr', 'GENEstart', 'GENEend',
                                       'GENEname', 'OVERLAP'])

    LocalGeneTEPairs = {}

    for pair in intersectdf.iterrows():
        TEname = pair[1][3]
        GENEid = data.gene_ids_of_gene_name(pair[1][7])[0]
        if GENEid in LocalGeneTEPairs.keys():
            LocalGeneTEPairs[GENEid].append(TEname)
        else:
            LocalGeneTEPairs[GENEid] = [TEname]

    tepatients = TransposableElement.columns.values.tolist()
    Genefilter = Gene.loc[:, tepatients]

    CorrTEid = []

    for gene in LocalGeneTEPairs.keys():
        for te in LocalGeneTEPairs[gene]:
            try:
                stat, pval = stats.pearsonr(Genefilter.loc[gene, :], LINE.loc[te, :])
                if stat > 0.70 and pval < 0.05:
                    CorrTEid.append(te)
            except:
                KeyError

    CorrTEid = list(set(CorrTEid))
    CleanTE = TransposableElement.drop(CorrTEid)

    return CleanTE

