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
	df = pd.read_csv('combine_pain_loose_all.csv')
	df.dropna(axis = 0, how = 'any', inplace = True)
	sig_vars1 = df[df.group2 == 1]
	sig_vars0 = + df[df.group2 == 0].sample(n = 900)
	sig_vars = pd.concat([sig_vars1, sig_vars0])
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	y = y.astype('int')

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('all_coefficients_loose.csv', index = False)

	THRESHOLD = 0.40
	y_pred = np.where(logreg.predict_proba(X_test)[:,1] > THRESHOLD, 1, 0)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))
	print('all idps loose with 900 control threshold 0.40 GML')

	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def svm_all():
	df = pd.read_csv('combine_pain_loose_all.csv')
	df.dropna(axis = 0, how = 'any', inplace = True)
	sig_vars1 = df[df.group2 == 1]
	sig_vars0 = + df[df.group2 == 0].sample(n = 900)
	sig_vars = pd.concat([sig_vars1, sig_vars0])
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	y = y.astype('int')

	from sklearn.model_selection import train_test_split
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)

	from sklearn.svm import SVC
	svclassifier = SVC(kernel = 'linear')
	svclassifier.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(svclassifier.coef_))], axis = 1)
	coefficients.to_csv('all_coefficients_svm_loose.csv', index = False)

	y_pred = svclassifier.predict(X_test)

	from sklearn.metrics import classification_report, confusion_matrix
	print('all idps loose with 900 control SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def glm_sig_vars_loose():
	df = pd.read_csv('sig_vars_loose.csv')
	df.dropna(axis = 0, how = 'any', inplace = True)
	sig_vars1 = df[df.group2 == 1]
	sig_vars0 = + df[df.group2 == 0].sample(n = 900)
	sig_vars = pd.concat([sig_vars1, sig_vars0])
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	y = y.astype('int')

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

	print('sig idps loose GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top30_loose():
	df = pd.read_csv('sig_vars_loose_top30.csv')
	df.dropna(axis = 0, how = 'any', inplace = True)
	sig_vars1 = df[df.group2 == 1]
	sig_vars0 = + df[df.group2 == 0].sample(n = 900)
	sig_vars = pd.concat([sig_vars1, sig_vars0])
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	y = y.astype('int')

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('top30_coefficients_loose.csv', index = False)

	THRESHOLD = 0.52
	y_pred = np.where(logreg.predict_proba(X_test)[:,1] > THRESHOLD, 1, 0)
	#y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('top 30 idps loose GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top40_loose():
	df = pd.read_csv('sig_vars_loose_top40.csv')
	df.dropna(axis = 0, how = 'any', inplace = True)
	sig_vars1 = df[df.group2 == 1]
	sig_vars0 = + df[df.group2 == 0].sample(n = 900)
	sig_vars = pd.concat([sig_vars1, sig_vars0])
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	y = y.astype('int')

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(logreg.coef_))], axis = 1)
	coefficients.to_csv('top40_coefficients_loose.csv', index = False)

	THRESHOLD = 0.5
	y_pred = np.where(logreg.predict_proba(X_test)[:,1] > THRESHOLD, 1, 0)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('top 40 idps loose GLM threshold .45')

	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def glm_top50():
	df = pd.read_csv('sig_vars_loose_top50.csv')
	df.dropna(axis = 0, how = 'any', inplace = True)
	sig_vars1 = df[df.group2 == 1]
	sig_vars0 = + df[df.group2 == 0].sample(n = 900)
	sig_vars = pd.concat([sig_vars1, sig_vars0])
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	y = y.astype('int')

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
	clf = LogisticRegression()
	clf.fit(X_train, y_train)
	coefficients = pd.concat([pd.DataFrame(X.columns),pd.DataFrame(np.transpose(clf.coef_))], axis = 1)
	coefficients.to_csv('top50_coefficients_loose.csv', index = False)

	#y_pred = logreg.predict(X_test)
	THRESHOLD = 0.60
	y_pred = np.where(clf.predict_proba(X_test)[:,1] > THRESHOLD, 1, 0)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(clf.score(X_test, y_test)))

	print('top 50 idps strict GLM threshold 0.45')

	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

	xx, yy = np.mgrid[-5:5:.01, -5:5:.01]
	grid = np.c_[xx.ravel(), yy.ravel()]
	probs = clf.predict_proba(grid)[:, 1].reshape(xx.shape)

	f, ax = plt.subplots(figsize=(8, 6))
	contour = ax.contourf(xx, yy, probs, 25, cmap="RdBu", vmin=0, vmax=1)
	ax_c = f.colorbar(contour)
	ax_c.set_label("$P(y = 1)$")
	ax_c.set_ticks([0, .25, .5, .75, 1])

	ax.scatter(X[100:,0], X[100:, 1], c=y[100:], s=50, cmap="RdBu", vmin=-.2, vmax=1.2, edgecolor="white", linewidth=1)

	ax.set(aspect="equal", xlim=(-5, 5), ylim=(-5, 5), xlabel="$X_1$", ylabel="$X_2$")


def main():
	#glm_all()
	#svm_all()
	#glm_sig_vars_loose()
	#glm_top30_loose()
	#glm_top40_loose()
	glm_top50()
main()