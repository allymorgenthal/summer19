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

def svm_all():
	sig_vars = pd.read_csv('combine_pain_control.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('all idps strict SVM')

	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def svm_nodelta():
	sig_vars = pd.read_csv('combine_pain_control_nodelta.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('idps w/o delta strict SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def svm_nofmri():
	sig_vars = pd.read_csv('combine_pain_control_nofmri.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('idps w/o delta fmri strict SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def svm_top20():
	sig_vars = pd.read_csv('sig_vars_strict_top20.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(svclassifier.coef_))], axis = 1)
	coefficients.to_csv('top20_coefficients_svm.csv', index = False)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('top 20 idps strict SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def svm_top30():
	sig_vars = pd.read_csv('sig_vars_strict_top30.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(svclassifier.coef_))], axis = 1)
	coefficients.to_csv('top30_coefficients_svm.csv', index = False)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('top 30 idps strict SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def svm_top40():
	sig_vars = pd.read_csv('sig_vars_strict_top40.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(svclassifier.coef_))], axis = 1)
	coefficients.to_csv('top40_coefficients_svm.csv', index = False)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('top 40 idps strict SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def svm_top50():
	sig_vars = pd.read_csv('sig_vars_strict_top50.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(svclassifier.coef_))], axis = 1)
	#coefficients.to_csv('top50_coefficients_svm.csv', index = False)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('top 50 idps strict SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def main():
	svm_all()
	svm_nodelta()
	svm_nofmri()
	svm_top20()
	svm_top30()
	svm_top40()
	svm_top50()
main()





