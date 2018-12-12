import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
from sklearn import preprocessing
from sklearn.utils import column_or_1d
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
def trainSVM(x,y):
    clf=svm.SVC(gamma='auto', C=100)
    clf.fit(x,y)
    return clf

if __name__=="__main__":
	
	data=pd.read_csv("RankedData.csv")
	from sklearn.feature_extraction.text import TfidfVectorizer
	tfidf = TfidfVectorizer(encoding='latin-1')

	model = LinearSVC()
	X_train, X_test, y_train, y_test = train_test_split(data['Requirement'], data['Ranking'],test_size=0.50, random_state=0)
	model.fit(tfidf.fit_transform(X_train), y_train)
	y_pred = model.predict(tfidf.transform(X_test))
	print(X_train)
	print(y_train.tolist())	
	values=X_test.index;
	print(y_test)
	print(y_pred)
	for i,j in zip(values,y_pred):
		data.iloc[i,data.columns.get_loc('Ranking')]=j
	data=data.sort_values(by='Ranking')
	print(data)
	data.to_csv("Rankedbysvm.csv")
	'''tfidf=TfidfVectoriser(stop_words="english")
	train_matrix=tfidf.fit_transform(data.Requirement)

	

	
	x=pd.get_dummies(data.Requirement)
	y=data.drop('Requirement',axis=1)
	y=y.values.ravel()
	#print(y.shape)
	x_train, x_test, y_train, y_test=train_test_split(x,y,test_size=0.30,random_state=0)
	#print(x_train)
	clf = SVC(kernel='linear')
	clf.fit(x,y)
	prediction=clf.predict(x_test)
	print(y_test)
	print(prediction)'''
	
