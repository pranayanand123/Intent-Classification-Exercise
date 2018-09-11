# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 19:51:11 2018

@author: pranay
"""

import pandas
import numpy
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import LinearSVC
from pandas import ExcelWriter



data = pandas.read_excel('sample.xlsx')

'''Exercise = pandas.read_excel('Exercise.xlsx')
X_Exercise = Exercise.iloc[:,0]
X_Exercise= X_Exercise.str.replace('[^\w\s]','')

X = data.iloc[:,0]
X = X.str.replace('[^\w\s]','')
Y1 = data.iloc[:,2]
Y2 = data.iloc[:,3]
Y3 = data.iloc[:,4]

count_vect1 = CountVectorizer()
count_vect1.fit_transform(X)
print(count_vect1.vocabulary_)

vector = count_vect1.transform(X)
print(vector.shape)
print(type(vector))
sample = vector.toarray()

lb_make1 = LabelEncoder()
Y1 = lb_make1.fit_transform(Y1)
classifier1 = MultinomialNB()
classifier1.fit(sample, Y1)
Y_Exercise = classifier1.predict(count_vect1.transform(X_Exercise))
Y_Exercise = pandas.Series(Y_Exercise)
Y_Exercise = Y_Exercise.apply(lambda x: 'complex' if x==0 else 'simple')
writer = pandas.ExcelWriter('Exercise.xlsx', engine='openpyxl')
Exercise.to_excel(writer, startcol=0,index=False)
Y_Exercise.to_excel(writer, startcol=1,index=False)
writer.save()'''

count_vect = CountVectorizer()
X_train_counts = count_vect.fit_transform(data['Question'])
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
clf2 = LinearSVC().fit(X_train_tfidf, data['Cat2'])
X_test = pandas.read_excel('Exercise.xlsx').iloc[:,0]

cat2 = clf2.predict(count_vect.transform(X_test))
cat2 = pandas.Series(cat2)

clf1 = LinearSVC().fit(X_train_tfidf, data['Cat1'])
cat1 = clf1.predict(count_vect.transform(X_test))
cat1 = pandas.Series(cat1)

clf3 = LinearSVC().fit(X_train_tfidf, data['Cat3'])
cat3 = clf3.predict(count_vect.transform(X_test))
cat3 = pandas.Series(cat3)
frame = pandas.concat([X_test,pandas.read_excel('Exercise.xlsx').iloc[:,1],cat1,cat2,cat3], axis=1)

writer2 = ExcelWriter('Exercise_Results.xlsx')
frame.to_excel(writer2,'Exercise_Results',index = False)
writer2.save()




