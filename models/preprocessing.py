import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.model_selection import train_test_split
from script.dataPrep import loadData

def preprocessing(filepath):

    data = loadData(filepath)
    X = data.iloc[:, 1]
    y = data.iloc[:, 2]

    vectorizer = CountVectorizer(stop_words='english')
    X_vectorized = vectorizer.fit_transform(X)

    tfidf = TfidfTransformer()
    X_tfidf = tfidf.fit_transform(X_vectorized)
    X_tfidf = X_tfidf.todense()

    X_tfidf = np.asarray(X_tfidf)

    X = X_tfidf[:, :]
    return X, y