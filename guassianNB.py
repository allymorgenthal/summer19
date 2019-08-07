import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, log_loss

df = pd.read_csv('combine_pain_loose_all.csv')
df.dropna(axis = 0, how = 'any', inplace = True)
sig_vars1 = df[df.group2 == 1]
sig_vars0 = + df[df.group2 == 0].sample(n = 900)
sig_vars = pd.concat([sig_vars1, sig_vars0])
X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
y = sig_vars['group2']
y = y.astype('int')

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)


clf = GaussianNB()
clf.fit(X, y)
y_pred = clf.predict(X_test)


acc = accuracy_score(y_test, y_pred)
print("Accuracy: {:.4%}".format(acc))

from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(y_test, y_pred)

print(confusion_matrix)
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))