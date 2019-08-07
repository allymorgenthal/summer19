import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neural_network import MLPClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.gaussian_process import GaussianProcessClassifier
from sklearn.gaussian_process.kernels import RBF
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis


def glm_all():
	sig_vars = pd.read_csv('combine_pain_control.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('all_coefficients.csv', index = False)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('all idps strict GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))


def glm_nodelta():
	sig_vars = pd.read_csv('combine_pain_control_nodelta.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('nodelta_coefficients.csv', index = False)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('idps w/o delta strict GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))



def glm_nofmri():
	sig_vars = pd.read_csv('combine_pain_control_nofmri.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('nofmri_coefficients.csv', index = False)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('idps w/o delta and fmri strict GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top20():
	sig_vars = pd.read_csv('sig_vars_strict_top20.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('top20_coefficients.csv', index = False)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('top 20 idps strict GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top30():
	sig_vars = pd.read_csv('sig_vars_strict_top30.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('top30_coefficients.csv', index = False)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('top 30 idps strict GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top40():
	sig_vars = pd.read_csv('sig_vars_strict_top40.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('top40_coefficients.csv', index = False)

	THRESHOLD = 0.45
	y_pred = np.where(logreg.predict_proba(X_test)[:,1] > THRESHOLD, 1, 0)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('top 40 idps strict GLM threshold .45')

	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top50():
	sig_vars = pd.read_csv('sig_vars_strict_top50.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('top50_coefficients.csv', index = False)

	#y_pred = logreg.predict(X_test)
	THRESHOLD = 0.45
	y_pred = np.where(logreg.predict_proba(X_test)[:,1] > THRESHOLD, 1, 0)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('top 50 idps strict GLM threshold 0.45')

	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))


def main():
	#glm_all()
	#glm_nodelta()
	#glm_nofmri()
	#glm_top20()
	#glm_top30()
	glm_top40()
	#glm_top50()
main()