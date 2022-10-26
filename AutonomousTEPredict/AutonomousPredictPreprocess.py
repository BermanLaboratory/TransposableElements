# Preprocessing for autonomous Transposable Element Prediction

# Input
#TE: Tranposable element per loci expression matrix with samples as columns and individual TE expression as rows.
    # Column names should be sample IDs, Row names should be TE names and genomic locations ('


import pandas as pd

LINE1 = pd.read_csv('TransposableElements/Data/tpmL1HS.csv')
print(LINE1.head(10))