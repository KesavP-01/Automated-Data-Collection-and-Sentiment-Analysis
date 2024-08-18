import joblib
from sklearn.metrics import accuracy_score
from preprocessing import preprocessing


model = joblib.load('models/nlpModel')

X, y = preprocessing('data/rev.csv')

yPred = model.predict(X)

accuracy = accuracy_score(y, yPred)
print(accuracy)
