from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


data = pd.read_csv('rev.csv')
test_data = pd.read_csv('reviews.csv')
test_data = test_data.dropna(how='any')
X = data.iloc[:,1]
y = data.iloc[:,2]




vectorizer = CountVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)
X_vec = X_vec.todense()



tfidf = TfidfTransformer()
X_tfidf = tfidf.fit_transform(X_vec)
X_tfidf = X_tfidf.todense()

X = X_tfidf[:, :]

clf = RandomForestClassifier()
clf = clf.fit(X, y)

X_test = test_data.iloc[:,1]
X_vec_test = vectorizer.transform(X_test)
X_vec_test = X_vec_test.todense()

X_tfidf_test = tfidf.fit_transform(X_vec_test)
X_tfidf_test = X_tfidf_test.todense()


y_pred = clf.predict(X_tfidf_test)



Overall_rating = test_data['Pred_Rating'].mean()
actual = test_data['Rating'].mean()
accuracy = accuracy_score(test_data[1], y_pred)
