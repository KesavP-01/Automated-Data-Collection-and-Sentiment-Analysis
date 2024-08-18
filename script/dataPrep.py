import pandas as pd
import numpy as np


def loadData(filepath):
    df = pd.read_csv(filepath)
    return df

def mergeDict(dict):
    df = pd.concat(dict.values(), ignore_index=True)
    return df

def processDF(data):
    data['Opinion'] = np.where(data['Rating'] <= 4, 'Negative', np.where(data['Rating'] <= 7, 'Neutral', 'Positive'))
    return data
