import pandas as pd

TEST = "data/test.txt"
TRAIN = "data/train.txt"


def load_data():
    df = pd.read_csv(TEST, sep=";", decimal=',')

    # set the correct typing to columns
    df['MontAnt'] = pd.to_numeric(df['MontAnt'], downcast='float')
    df['DAteTrAnsAction'] = pd.to_datetime(df['DAteTrAnsAction'])

    # useless columns
    df.drop(['ZIBZIN', 'IDAvisAutorisAtionCheque'], axis=1, inplace=True)
    return df

