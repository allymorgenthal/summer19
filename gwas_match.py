import pandas as pd
import numpy as np
import csv


def match():
	gwas1 = pd.read_csv('gwas1_imputed_collated.csv')
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval', sep = '\t', names = ["Gene", "Chr", "Sign", "Start", "Stop", "6", "7", "8"])

	print(genes.head())
	print(gwas1.head())

	file = open('matched genes.csv', "w+")

	for idx, row1 in gwas1.iterrows():
		for idx, row2 in genes.iterrows():
			if row1.Chr == row2.Chr:
				if (row1.Pos > row2.Start) & (row1.Pos < row2.Stop):
					file.write(row1, row2)

	file.to_csv('gwas1_genes.csv', index = False)


def match2_gwas1():
	gwas1 = pd.read_csv('gwas1_imputed_collated.csv')
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval', sep = '\t', names = ["Gene", "Chr", "Sign", "Start", "Stop", "6", "7", "8"])

	genes2 = genes.loc[~(genes.Chr == 'X') & ~(genes.Chr == 'Y') & ~(genes.Chr == 'MT')]

	genes2['Chr'] = genes2['Chr'].astype(int)
	#genes2.Chr.astype(int)

	print('hi')

	df3 = pd.merge(gwas1, genes2, on = ['Chr'])
	df3.to_csv('merged_gwas1_genes2.csv', index = False)
	
	print('hi')
	#file = df3.loc[(df3.Pos >= df3.Start) & (df3.Pos <= df3.Stop)]
	#file = df3.loc[(df3['Pos'] >= df3['Start']) & (df3['Pos'] <= df3['Stop'])]


	#file.to_csv('gwas1_genes2.csv', index = False)

def match3_gwas1():
	df = pd.read_csv('merged_gwas1_genes.csv')

	file3 = open('gwas1_genes3.csv', "w+")

	#for idx, row1 in df.iterrows():
	#	if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
	#		#line = [row1.Name, row1.Chr, row1.Pos, row1.Pval, row1.Gene, row1.Start, row1.Stop]
	#		file3.write(row1.Name + " ")
	#		file3.write(str(row1.Chr) + " ")
	#		file3.write(str(row1.Pos) + " ")
	#		file3.write(str(row1.Pval) + " ")
	#		file3.write(row1.Gene + " ")
	#		file3.write(str(row1.Start) + " ")
	#		file3.write(str(row1.Stop) + " ")
	#		file3.write('\n')
	#file3.close()

	with open('gwas1_genes3.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in df.iterrows():
			if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
				gene_writer.writerow(row1)

def merge_gwas2():
	gwas1 = pd.read_csv('gwas2_imputed_collated.csv')
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval', sep = '\t', names = ["Gene", "Chr", "Sign", "Start", "Stop", "6", "7", "8"])

	genes2 = genes.loc[~(genes.Chr == 'X') & ~(genes.Chr == 'Y') & ~(genes.Chr == 'MT')]

	genes2['Chr'] = genes2['Chr'].astype(int)

	print('hi')

	df3 = pd.merge(gwas1, genes2, on = ['Chr'])
	print('hi')
	df3.to_csv('merged_gwas2_genes.csv', index = False)

def match_gwas2():
	df = pd.read_csv('merged_gwas2_genes.csv')

	file3 = open('gwas2_genes.csv', "w+")

	with open('gwas2_genes.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in df.iterrows():
			if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
				gene_writer.writerow(row1)

def merge_gwas5():
	gwas1 = pd.read_csv('gwas5_imputed_collated.csv')
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval', sep = '\t', names = ["Gene", "Chr", "Sign", "Start", "Stop", "6", "7", "8"])

	genes2 = genes.loc[~(genes.Chr == 'X') & ~(genes.Chr == 'Y') & ~(genes.Chr == 'MT')]

	genes2['Chr'] = genes2['Chr'].astype(int)

	print('hi')

	df3 = pd.merge(gwas1, genes2, on = ['Chr'])
	df3.to_csv('merged_gwas5_genes.csv', index = False)


def match_gwas5():
	df = pd.read_csv('merged_gwas5_genes.csv', usecols = ['Name', "Chr", "Pos", "Pval", "AAF", "Gene", "Start", "Stop"])

	file3 = open('gwas5_genes.csv', "w+")

	with open('gwas5_genes.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in df.iterrows():
			if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
				gene_writer.writerow(row1)

def merge_gwas3():
	gwas1 = pd.read_csv('gwas3_imputed_collated.csv')
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval', sep = '\t', names = ["Gene", "Chr", "Sign", "Start", "Stop", "6", "7", "8"])

	genes2 = genes.loc[~(genes.Chr == 'X') & ~(genes.Chr == 'Y') & ~(genes.Chr == 'MT')]

	genes2['Chr'] = genes2['Chr'].astype(int)

	print('hi')

	df3 = pd.merge(gwas1, genes2, on = ['Chr'])
	df3.to_csv('merged_gwas3_genes.csv', index = False)


def match_gwas3():
	df = pd.read_csv('merged_gwas3_genes.csv', usecols = ['Name', "Chr", "Pos", "Pval", "AAF", "Gene", "Start", "Stop"])

	file3 = open('gwas3_genes.csv', "w+")

	with open('gwas3_genes.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in df.iterrows():
			if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
				gene_writer.writerow(row1)

def delete_col_gwas3():
	df = pd.read_csv('merged_gwas3_genes.csv')
	keep_col = ['Name', "Chr", "Pos", "Pval", "AAF", "Gene", "Start", "Stop"]
	new_df = df[keep_col]
	new_df.to_csv('gwas3_keepcol.csv', index = False)

def delete_col_gwas5():
	df = pd.read_csv('merged_gwas5_genes.csv')
	keep_col = ['Name', "Chr", "Pos", "Pval", "AAF", "Gene", "Start", "Stop"]
	new_df = df[keep_col]
	new_df.to_csv('gwas5_keepcol.csv', index = False)


def match_hard():
	gwas1 = pd.read_csv('gwas1_imputed_collated.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval.csv', usecols = [0, 1, 3, 4], names = ["Gene", "Chr", "Start", "Stop"], )

	#print(genes.head())
	#print(gwas1.head())

	#file = open('matched_genes1.csv', "w+")


	#gwas1 = open('gwas1_imputed_collated.csv')

	#with open('Ensembl85.whiteList.transcripts.interval.csv', usecols = [0, 1, 3, 4], names = ["Gene", "Chr", "Start", "Stop"]):
	#gwas1_dict = {}
	#for line in gwas1:
	#	gwas1_dict[gwas1["Name"]] == gwas1["Pos"]
	#print(gwas1_dict)

	genes2 = genes.loc[~(genes.Chr == 'X') & ~(genes.Chr == 'Y') & ~(genes.Chr == 'MT')]

	genes2['Chr'] = genes2['Chr'].astype(int)

	for idx, row1 in gwas1.iterrows():
		for idx, row2 in genes2.iterrows():
			if (row1.Chr == row2.Chr):
				if (row1.Pos >= row2.Start) & (row1.Pos <= row2.Stop):
					df3 = pd.merge(row1, row2, on = ["Chr"])

	df3.to_csv('gwas1_hard.csv', index = False)

	#for idx, row1 in gwas1.iterrows():
	#	for idx, row2 in genes.iterrows():
	#		if (row1.Pos > row2.Start) & (row1.Pos < row2.Stop):
	#			file.write(row1, row2)

	#ile.to_csv('gwas1_genes.csv', index = False)

def match_try():
	column_dtypes = {'Gene': 'category', 'Chr': 'uint32', 'Start':'uint32', 'Stop':'uint32'}
	gwas1 = pd.read_csv('gwas1_imputed_collated.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('genes_individual.csv', dtype = column_dtypes)


	merged = pd.merge(gwas1, genes, how = "left", on = ['Chr'])
	print('hi')

	with open('gwas1_genes_try.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in merged.iterrows():
			if (row1.Pos >= row1.Start - 250000) & (row1.Pos <= row1.Stop + 250000):
				print(row1)
				gene_writer.writerow(row1)


def match_hard2():
	gwas2 = pd.read_csv('gwas2_imputed_collated.csv', usecols = ["Name", "Chr", "Pos"])
	genes = pd.read_csv('Ensembl85.whiteList.transcripts.interval.csv', usecols = [0, 1, 3, 4], names = ["Gene", "Chr", "Start", "Stop"])

	genes2 = genes.loc[~(genes.Chr == 'X') & ~(genes.Chr == 'Y') & ~(genes.Chr == 'MT')]

	genes2['Chr'] = genes2['Chr'].astype(int)

	with open('gwas2_genes_hard.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in gwas2.iterrows():
			for idx, row2 in genes2.iterrows():
				if (row1.Chr == row2.Chr):
					if (row1.Pos >= row2.Start) & (row1.Pos <= row2.Stop):
						gene_writer.writerow(row)

def match_try2():
	column_dtypes = {'Gene': 'category', 'Chr': 'uint32', 'Start':'uint32', 'Stop':'uint32'}
	gwas2 = pd.read_csv('gwas2_imputed_collated.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('genes_individual.csv', dtype = column_dtypes)


	merged = pd.merge(gwas2, genes, how = "left", on = ['Chr'])
	print('hi')


	with open('gwas2_genes_try.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in merged.iterrows():
			if (row1.Pos >= row1.Start - 250000) & (row1.Pos <= row1.Stop + 250000):
				print(row1)
				gene_writer.writerow(row1)

def match_try5():
	column_dtypes = {'Gene': 'category', 'Chr': 'uint32', 'Start':'uint32', 'Stop':'uint32'}
	gwas5 = pd.read_csv('gwas5_imputed_collated.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('genes_individual.csv', dtype = column_dtypes)


	merged = pd.merge(gwas5, genes, how = "left", on = ['Chr'])
	print('hi')


	with open('gwas5_genes_try.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in merged.iterrows():
			if (row1.Pos >= row1.Start - 250000) & (row1.Pos <= row1.Stop + 250000):
				print(row1)
				gene_writer.writerow(row1)

def match_try3():
	column_dtypes = {'Gene': 'category', 'Chr': 'uint32', 'Start':'uint32', 'Stop':'uint32'}
	gwas3 = pd.read_csv('gwas3_imputed_collated.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('genes_individual.csv', dtype = column_dtypes)


	merged = pd.merge(gwas3, genes, how = "left", on = ['Chr'])
	print('hi')


	with open('gwas3_genes_try.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in merged.iterrows():
			if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
				print(row1)
				gene_writer.writerow(row1)

def add_pval():
	genes1 = pd.read_csv('gwas1_genes_try.csv')
	gwas1 = pd.read_csv('gwas1_imputed_collated.csv',  usecols = ["Name", "Pval"])

	result = pd.merge(genes1, gwas1, on = ['Name'])

	result.to_csv("gwas1_genes_wp.csv", index = False)

def find_unmatch1():
	gwas1 = pd.read_csv('gwas1_imputed_collated.csv')
	found_genes = pd.read_csv('gwas1_genes_exact.csv')

	result = gwas1[~gwas1.Name.isin(found_genes.Name.values)]

	result.to_csv('unmatched_gwas1.csv', index = False)

def find_unmatch2():
	gwas2 = pd.read_csv('gwas2_imputed_collated.csv')
	found_genes2 = pd.read_csv('gwas2_genes_exact.csv')

	result = gwas2[~gwas2.Name.isin(found_genes2.Name.values)]

	result.to_csv('unmatched_gwas2.csv', index = False)

def find_unmatch3():
	gwas3 = pd.read_csv('gwas3_imputed_collated.csv')
	found_genes3 = pd.read_csv('gwas3_genes_exact.csv')

	result = gwas3[~gwas3.Name.isin(found_genes3.Name.values)]

	result.to_csv('unmatched_gwas3.csv', index = False)

def find_unmatch5():
	gwas5 = pd.read_csv('gwas5_imputed_collated.csv')
	found_genes5 = pd.read_csv('gwas5_genes_exact.csv')

	result = gwas5[~gwas5.Name.isin(found_genes5.Name.values)]

	result.to_csv('unmatched_gwas5.csv', index = False)


def match4():
	column_dtypes = {'Gene': 'category', 'Chr': 'uint32', 'Start':'uint32', 'Stop':'uint32'}
	gwas4 = pd.read_csv('gwas4_e3.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('genes_individual.csv', dtype = column_dtypes)


	merged = pd.merge(gwas4, genes, how = "left", on = ['Chr'])
	print('hi')


	with open('gwas4_genes.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in merged.iterrows():
			if (row1.Pos >= row1.Start) & (row1.Pos <= row1.Stop):
				print(row1)
				gene_writer.writerow(row1)

def match4_expand():
	column_dtypes = {'Gene': 'category', 'Chr': 'uint32', 'Start':'uint32', 'Stop':'uint32'}
	gwas4 = pd.read_csv('gwas4_e3.csv', usecols = ["Name", "Chr", "Pos", "Pval"])
	genes = pd.read_csv('genes_individual.csv', dtype = column_dtypes)


	merged2 = pd.merge(gwas4, genes, how = "left", on = ['Chr'])
	print('hi')


	with open('gwas4_genes_expand.csv', mode='w') as gene_file:
		gene_writer = csv.writer(gene_file, delimiter=',', quotechar='"')
		for idx, row1 in merged2.iterrows():
			if (row1.Pos >= row1.Start - 250000) & (row1.Pos <= row1.Stop + 250000):
				print(row1)
				gene_writer.writerow(row1)


def main():
	#match()
	#match2()
	#match3_gwas1()
	#merge_gwas2()
	#match_gwas2()
	#merge_gwas5()
	#match_gwas5()
	#merge_gwas3()
	#match_gwas3()
	#delete_col_gwas3()
	#delete_col_gwas5()
	#match_hard()
	#match_hard2()
	#match_try()
	#match_try2()
	#match_try3()
	#match_try5()
	#add_pval()
	#find_unmatch1()
	#find_unmatch2()
	#find_unmatch3()
	#find_unmatch5()
	#match4()
	match4_expand()


main()