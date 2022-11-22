def UROMOLreorder(ID, df):

    # inputs
    # ID: list of UROMOL df column IDs
    # df: Transcript-omic dataframe with UROMOL column ids

    IDs = sorted(ID)

    strIDs = []

    for ID in IDs:
        if len(str(ID)) == 1:
            ID = 'U000' + str(ID)
            strIDs.append(ID)
        elif len(str(ID)) == 2:
            ID = 'U00' + str(ID)
            strIDs.append(ID)
        elif len(str(ID)) == 3:
            ID = 'U0' + str(ID)
            strIDs.append(ID)
        elif len(str(ID)) == 4:
            ID = 'U' + str(ID)
            strIDs.append(ID)

    df = df[strIDs]
    return df