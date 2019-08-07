import pandas as pd

def main():
	file1 = pd.read_table('IDPs.txt', 
		engine = 'python',
		sep = ' ',
		header = 0,
		index_col = 0, 
		na_values = ['NA'])
	#print (file1)
	#file1.to_excel('IDPs_table.xlsx', engine='xlsxwriter')

	writer = pd.ExcelWriter('IDPs_table2.xlsx', engine='xlsxwriter')

	writer.book.use_zip64()
	file1.to_excel(writer, sheet_name='Data')
	writer.save()

#	file1 = open('idps_deconf1.fam')
#	file2 = open('IDPs_table.txt', "w+")
#	for line in file1:
#	file2.write(file1)
#		fields = line.split("\n")
#		for i in fields:
#			file2.write(i)
#			file2.write("\n")
#	file1.close()
#	file2.close()
main()