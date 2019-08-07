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


def svm():
	sig_vars = pd.read_csv('sig_vars_group2.csv')
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
	print('All sigvars for strict group SVM')
	print(confusion_matrix(y_test, y_pred))
	print(classification_report(y_test, y_pred))

def glm_strict():
	sig_vars = pd.read_csv('sig_vars_group2.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	print('all sigvars strict GLM')
	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

	from sklearn.metrics import roc_auc_score
	from sklearn.metrics import roc_curve
	logit_roc_auc = roc_auc_score(y_test, logreg.predict(X_test))
	fpr, tpr, thresholds = roc_curve(y_test, logreg.predict_proba(X_test)[:,1])
	plt.figure()
	plt.plot(fpr, tpr, label='Logistic Regression (area = %0.2f)' % logit_roc_auc)
	plt.plot([0, 1], [0, 1],'r--')
	plt.xlim([0.0, 1.0])
	plt.ylim([0.0, 1.05])
	plt.xlabel('False Positive Rate')
	plt.ylabel('True Positive Rate')
	plt.title('Receiver operating characteristic')
	plt.legend(loc="lower right")
	plt.savefig('Log_ROC')
	plt.show()


def glm_loose():
	sig_vars = pd.read_csv('sig_vars_loose.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']
	print(X.head())
	print(y.tail())


	from sklearn.linear_model import LogisticRegression
	from sklearn import metrics
	from sklearn.model_selection import train_test_split


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
	logreg = LogisticRegression()
	logreg.fit(X_train, y_train)

	y_pred = logreg.predict(X_test)
	print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(logreg.score(X_test, y_test)))

	from sklearn.metrics import confusion_matrix
	confusion_matrix = confusion_matrix(y_test, y_pred)
	print(confusion_matrix)

	from sklearn.metrics import classification_report
	print(classification_report(y_test, y_pred))

def test():

	h = .02  # step size in the mesh

	names = ["Nearest Neighbors", "Linear SVM", "RBF SVM", "Gaussian Process",
         "Decision Tree", "Random Forest", "Neural Net", "AdaBoost",
         "Naive Bayes", "QDA"]

	classifiers = [
    	KNeighborsClassifier(3),
    	SVC(kernel="linear", C=0.025),
    	SVC(gamma=2, C=1),
    	GaussianProcessClassifier(1.0 * RBF(1.0)),
    	DecisionTreeClassifier(max_depth=5),
    	RandomForestClassifier(max_depth=5, n_estimators=10, max_features=1),
    	MLPClassifier(alpha=1, max_iter=1000),
    	AdaBoostClassifier(),
    	GaussianNB(),
    	QuadraticDiscriminantAnalysis()]

	sig_vars = pd.read_csv('sig_vars_group2.csv')
	sig_vars.dropna(axis = 0, how = 'any', inplace = True)
	X = sig_vars.drop(['group', 'eid', 'group2'], axis = 1)
	y = sig_vars['group2']

	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.4, random_state=0)




	for name, clf in zip(names, classifiers):
		clf.fit(X_train, y_train)
		score = clf.score(X_test, y_test)

		# Plot the decision boundary. For that, we will assign a color to each
		# point in the mesh [x_min, x_max]x[y_min, y_max].

		ax = plt.subplot()
		# Put the result into a color plot
		# Plot the training points
		ax.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cm_bright, edgecolors='k')
		# Plot the testing points
		ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap=cm_bright, edgecolors='k', alpha=0.6)

		ax.set_xticks(())
		ax.set_yticks(())
		if ds_cnt == 0:
			ax.set_title(name)
		i += 1

	plt.tight_layout()
	plt.show()

def main():
	#svm()
	#glm_strict()
	glm_loose()
	#test()
main()

#datarobot
#print out coefficients
#unsupervised learning to see differences
#look at threshold
