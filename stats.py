## Import the packages
import numpy as np
from scipy.stats import ttest_ind
import pandas as pd
import csv
from statsmodels.stats import multitest

#stats function i used to run ttests and benjamini hotchberg correction
def stat_10col():
	#OA_grey_vol = pd.read_csv("OA_10col_wIDPs.csv", usecols=['FID','Volume_of_grey_matter_(normalised_for_head_size)']).set_index('FID')
	#control_grey_vol = pd.read_csv("control_10col_wIDPs.csv", usecols=['FID','Volume_of_grey_matter_(normalised_for_head_size)']).set_index('FID')
	OA = pd.read_csv("OA_10col_wIDPs.csv")
	control = pd.read_csv("control_10col_wIDPs.csv")


	#ttest = stats.ttest_ind(OA.value[OA.names == 'Volume_of_grey_matter_(normalised_for_head_size)'], control.value[control.names == 'Volume_of_grey_matter_(normalised_for_head_size)'])

	#ttest = ttest_ind(OA_grey_vol.values, control_grey_vol.values)
	#ttest = ttest_ind(OA['Volume_of_grey_matter_(normalised_for_head_size)'], control['Volume_of_grey_matter_(normalised_for_head_size)'])
	#print(ttest)

	with open("OA_10col_wIDPs.csv") as f:
		reader = csv.reader(f)
		cols = next(reader)

	#file2 = open('ttests.csv', "w+")
	file3 = open('significant_ttests.csv', "w+")
	file4 = open('bonferroni.csv', "w+")
	#file5 = open("fdr.csv", "w+")
	pvalues = []


	with open('ttest.csv', mode = 'w') as ttest_file:
		for i in range(31, len(cols)):
			ttest = ttest_ind(OA[cols[i]].dropna(), control[cols[i]].dropna())
			
			writer = csv.writer(ttest_file, delimiter = ',', quotechar = '"')
			writer.writerow([cols[i], ttest.pvalue])
		
		#file2.write("TTest on " + cols[i] + " ")
		#file2.write(str(ttest.pvalue))
		#file2.write('\n')

			pvalues.append(ttest.pvalue)

		#print("OA", cols[i],", control", cols[i], ", ", ttest)

			if ttest.pvalue < 0.05:
				file3.write("TTest on " + cols[i] + " ")
				file3.write(str(ttest))
				file3.write('\n')

			if (ttest.pvalue * 2655) < 0.05:
				file4.write("TTest on " + cols[i] + " ")
				file4.write(str(ttest.pvalue * 2655))
				file4.write('\n')

	pvalues.sort()
	#print(pvalues)

	fdr = multitest.fdrcorrection(pvalues, alpha = 0.10, is_sorted = True)
	with open('fdr_pvalues.csv', mode = 'w') as fdr_file:
		writer = csv.writer(fdr_file, delimiter = ',', quotechar = '"')
		l = list(fdr)
		x = zip(*l)
		print(x)
		for i in x:
			writer.writerow([i])


	#file2.close()
	file3.close()
	file4.close()
	#file5.close()

def stat_wpain():
	OA = pd.read_csv("OA_and_3mon_pain.csv")
	control = pd.read_csv("control_no_pain.csv")


	with open("OA_and_3mon_pain.csv") as f:
		reader = csv.reader(f)
		cols = next(reader)

	file3 = open('significant_ttests_wpain.csv', "w+")
	#file4 = open('bonferroni.csv', "w+")
	pvalues = []


	with open('ttest_wpain.csv', mode = 'w') as ttest_file:
		for i in range(55, len(cols)):
			ttest = ttest_ind(OA[cols[i]].dropna(), control[cols[i]].dropna())
			
			writer = csv.writer(ttest_file, delimiter = ',', quotechar = '"')
			writer.writerow([cols[i], ttest.pvalue])
		
		#file2.write("TTest on " + cols[i] + " ")
		#file2.write(str(ttest.pvalue))
		#file2.write('\n')

			pvalues.append(ttest.pvalue)

		#print("OA", cols[i],", control", cols[i], ", ", ttest)

			if ttest.pvalue < 0.05:
				file3.write("TTest on " + cols[i] + " ")
				file3.write(str(ttest))
				file3.write('\n')

			#if (ttest.pvalue * 2655) < 0.05:
				#file4.write("TTest on " + cols[i] + " ")
				#file4.write(str(ttest.pvalue * 2655))
				#file4.write('\n')

	pvalues.sort()
	file3.close()
	#print(pvalues)

	fdr = multitest.fdrcorrection(pvalues, alpha = 0.10, is_sorted = True)
	with open('fdr_pvalues_wpain.csv', mode = 'w') as fdr_file:
		writer = csv.writer(fdr_file, delimiter = ',', quotechar = '"')
		l = list(fdr)
		x = zip(*l)
		print(x)
		for i in x:
			writer.writerow([i])


	#file4.close()

def combine_wlabel():
	df = pd.read_csv("OA_and_3mon_pain.csv", low_memory = False)
	df2 = pd.read_csv("control_no_pain.csv", low_memory = False)

	result = pd.concat([df, df2])

	result.to_csv("combine_OA_control.csv", index = False)

def stat_all_periph():
	PP = pd.read_csv("all_periph_pain_final.csv")
	CG = pd.read_csv("control_final.csv")


	with open("all_periph_pain_final.csv") as f:
		reader = csv.reader(f)
		cols = next(reader)

	file3 = open('significant_ttests_periph.csv', "w+")
	#file4 = open('bonferroni.csv', "w+")
	pvalues = []


	with open('ttest_periph.csv', mode = 'w') as ttest_file:
		for i in range(33, len(cols)):
			ttest = ttest_ind(PP[cols[i]].dropna(), CG[cols[i]].dropna())
			
			writer = csv.writer(ttest_file, delimiter = ',', quotechar = '"')
			writer.writerow([cols[i], ttest.pvalue])
		
		#file2.write("TTest on " + cols[i] + " ")
		#file2.write(str(ttest.pvalue))
		#file2.write('\n')

			pvalues.append(ttest.pvalue)

		#print("OA", cols[i],", control", cols[i], ", ", ttest)

			if ttest.pvalue < 0.05:
				file3.write("TTest on " + cols[i] + " ")
				file3.write(str(ttest))
				file3.write('\n')

			#if (ttest.pvalue * 2655) < 0.05:
				#file4.write("TTest on " + cols[i] + " ")
				#file4.write(str(ttest.pvalue * 2655))
				#file4.write('\n')

	pvalues.sort()
	file3.close()
	#print(pvalues)

	fdr = multitest.fdrcorrection(pvalues, alpha = 0.10, is_sorted = True)
	with open('fdr_pvalues_periph.csv', mode = 'w') as fdr_file:
		writer = csv.writer(fdr_file, delimiter = ',', quotechar = '"')
		l = list(fdr)
		x = zip(*l)
		print(x)
		for i in x:
			writer.writerow([i])

def combine_wlabel2():
	df = pd.read_csv("all_periph_pain_final.csv", low_memory = False)
	df2 = pd.read_csv("control_final.csv", low_memory = False)

	result = pd.concat([df, df2])

	result.to_csv("combine_pain_control.csv", index = False)


def stat_loose_cont():
	PP = pd.read_csv("all_periph_pain_final.csv")
	CG = pd.read_csv("loose_control_IDPs.csv")


	with open("all_periph_pain_final.csv") as f:
		reader = csv.reader(f)
		cols = next(reader)

	file3 = open('significant_ttests_loose.csv', "w+")
	#file4 = open('bonferroni.csv', "w+")
	pvalues = []


	with open('ttest_loose.csv', mode = 'w') as ttest_file:
		for i in range(21, len(cols)):
			ttest = ttest_ind(PP[cols[i]].dropna(), CG[cols[i]].dropna())
			
			writer = csv.writer(ttest_file, delimiter = ',', quotechar = '"')
			writer.writerow([cols[i], ttest.pvalue])
		
		#file2.write("TTest on " + cols[i] + " ")
		#file2.write(str(ttest.pvalue))
		#file2.write('\n')

			pvalues.append(ttest.pvalue)

		#print("OA", cols[i],", control", cols[i], ", ", ttest)

			if ttest.pvalue < 0.05:
				file3.write("TTest on " + cols[i] + " ")
				file3.write(str(ttest))
				file3.write('\n')

			#if (ttest.pvalue * 2655) < 0.05:
				#file4.write("TTest on " + cols[i] + " ")
				#file4.write(str(ttest.pvalue * 2655))
				#file4.write('\n')

	pvalues.sort()
	file3.close()
	#print(pvalues)

	fdr = multitest.fdrcorrection(pvalues, alpha = 0.10, is_sorted = True)
	with open('fdr_pvalues_loose.csv', mode = 'w') as fdr_file:
		writer = csv.writer(fdr_file, delimiter = ',', quotechar = '"')
		l = list(fdr)
		x = zip(*l)
		print(x)
		for i in x:
			writer.writerow([i])


def main():
	#stat_wpain()
	#combine_wlabel()
	#stat_all_periph()
	#combine_wlabel2()
	stat_loose_cont()
main()









