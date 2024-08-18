from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from preprocessing import preprocessing


def model(filepath):

    X, y = preprocessing(filepath)

    clf = RandomForestClassifier()
    clf.fit(X, y)
    return clf






