import pandas as pd 
import numpy as np

#def main():
#	file1 = "ukb24295.csv"
#	chunksize = 1000
#	print(pd.read_csv(file1, chunksize=chunksize))
#main()

#def read_in_chunks(file_object, chunk_size=1024):
#    """Lazy function (generator) to read a file piece by piece.
#    Default chunk size: 1k."""
#    while True:
#        data = file_object.read(chunk_size)
#        if not data:
#            break
 #       yield data


#f = open('really_big_file.dat')
#for piece in read_in_chunks(f):
#    process_data(piece)

#import pandas as pd
#df = pd.read_csv(csv_file)
#saved_column = df.[3799] #you can also use df['column_name']


#separate columns with medical information like diagonsis
def seperate_medical():
	df = pd.read_csv("ukb24295.csv", usecols = ['eid', "31-0.0", "34-0.0", "48-0.0", "50-0.0", "1707-0.0", "3160-0.0",'20002-0.0', '20002-0.1', '20002-0.2', '20002-0.3', '20002-0.4', '20002-0.5', '20002-0.6', '20002-0.7', '20002-0.8', '20002-0.9', '20002-0.10', '41202-0.0', '41202-0.1', '41202-0.2', '41202-0.3', '41202-0.4', '41202-0.5', '41202-0.6', '41202-0.7', '41202-0.8', '41202-0.9', '41202-0.10'])
	df.to_csv('clinical_columns.csv', index = False)

def first_1000():
	#df2 = pd.read_csv("UKB500K_sampleID_RGCPID.csv")
	#rgcpID = df2.loc[df2['rgcpID']]
	#result = pd.concat([df, df2], axis = 1)
	
	#df.sort_values(by = ['eid'])
	#df.insert(1, 'rgcpID', rgcpID)
	file1 = open("ukb24295.csv")
	file2 = open('first_1000.csv', "w+")
	for i in range(0, 1000):
		line = file1.readline()
		file2.write(line)
		i += 1

def first_40000():
	file1 = open("ukb24295.csv")
	file2 = open('first_40000.csv', "w+")
	for i in range(0, 40000):
		line = file1.readline()
		file2.write(line)
		i += 1

def find_OA_RA_1000():
	df = pd.read_csv("first_1000.csv")
	df2 = pd.read_csv("UKB500K_sampleID_RGCPID.csv")
	
	#adding regeneron codes to UKB codes
	df.insert(1, 'rgcpID', np.nan)
	print(df.head())
	
	#for row1 in df.itertuples():
	#	for row2 in df2.itertuples():
	for idx, row1 in df.iterrows():
		for idx, row2 in df2.iterrows():
			if row1.eid == row2.eid:
				df.set_value(idx, 'rgcpID', row2.rgcpID) #has error that set value may be removed at some point
				print(df.head())
				#df.at[index, 'rgcpID'] = row2.rgcpID

	#for i in range(len(df)):
	#	for j in range(len(df2)):
	#		if df.loc[[i],["eid"]] == df2.loc[[j],['eid']]:
	#			df.loc[[i],['rgcpID']] = df2.loc[[j],['rgcpID']]
	#			j += 1
	#		else:
	#			j += 1
	#	i += 1

	print(df.head()) 
	rheumatoid_arthritis_array = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	other_athrosis_array = ['M1900', 'M1901', 'M1902', 'M1903', 'M1904', 'M1905', 'M1906', 'M1907', 'M1908', 'M1909']
	coxarthrosis_array = ['M160', 'M161', 'M162', 'M164', 'M165', 'M166', 'M167', 'M169']
	gonarthrosis_array = ['M170', 'M171', 'M172', 'M173', 'M174', 'M175', 'M179']
	arthritis_array = coxarthrosis_array + gonarthrosis_array + rheumatoid_arthritis_array + other_athrosis_array
	#file2 = df.loc[df["41202-0.0"] == 'M161']
	#file2 = df.loc[df['eid'] == 1400897]
	file2 = df.loc[df['41202-0.0'].isin(arthritis_array)]
	file2.to_csv('OA_RA_1000.csv', index = False)

#find hospital record reported OA
def find_OA_hosp():
	df = pd.read_csv("clinical_columns_regID.csv", low_memory = False, delimiter=',', encoding="utf-8-sig")
	#print(df.head())
	rheumatoid_arthritis_array = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	other_athrosis_array = ['M1900', 'M1901', 'M1902', 'M1903', 'M1904', 'M1905', 'M1906', 'M1907', 'M1908', 'M1909']
	coxarthrosis_array = ['M160', 'M161', 'M162', 'M164', 'M165', 'M166', 'M167', 'M169']
	gonarthrosis_array = ['M170', 'M171', 'M172', 'M173', 'M174', 'M175', 'M179']
	arthritis_array = coxarthrosis_array + gonarthrosis_array + other_athrosis_array
	#file2 = df.loc[df["41202-0.0"] == 'M161']
	#file2 = df.loc[df['eid'] == 1400897]
	file2 = df.loc[(df['41202-0.0'].isin(arthritis_array)) | (df['41202-0.1'].isin(arthritis_array)) | (df['41202-0.2'].isin(arthritis_array)) | (df['41202-0.3'].isin(arthritis_array)) | (df['41202-0.4'].isin(arthritis_array)) | (df['41202-0.5'].isin(arthritis_array)) | (df['41202-0.6'].isin(arthritis_array)) | (df['41202-0.7'].isin(arthritis_array)) | (df['41202-0.8'].isin(arthritis_array)) | (df['41202-0.9'].isin(arthritis_array)) | (df['41202-0.10'].isin(arthritis_array))]
	file2.to_csv('OA_hospital.csv', index = False)

	#file1 = open("OA_RA_1000.csv")
	#file2 = open("UKB500K_sampleID_RGCPID.csv")
	#file3 = open("OA_RA_converted.csv", 'w+')
	#file1.readline()
	#file2
	#for line1 in file1:
	#	for line2 in file2:
	#		if (line1["eid"]) == (line2["sampleID"]):
	#			line1["eid"] = line2["rgcpID"]

#find self reported OA
def find_OA_self():
	df = pd.read_csv("clinical_columns_regID.csv", low_memory = False, delimiter=',', encoding="utf-8-sig")
	OA = ['1465']
	file2 = df.loc[(df['20002-0.0'] == 1465) | (df['20002-0.1'] == 1465) | (['20002-0.2'] == 1465) | (['20002-0.3'] == 1465) | (['20002-0.4'] == 1465) | (['20002-0.5'] == 1465) | (['20002-0.6'] == 1465) | (['20002-0.7'] == 1465) | (['20002-0.8'] == 1465) | (['20002-0.9'] == 1465) | (['20002-0.10'] == 1465)]
	file2.to_csv('OA_selfreport.csv', index = False)

#find people with blanks in all medical columns
def find_control():
	df = pd.read_csv("clinical_columns_regID.csv", low_memory = False, delimiter=',', encoding="utf-8-sig")
	#print(df.head())
	rheumatoid_arthritis_array = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	other_athrosis_array = ['M1900', 'M1901', 'M1902', 'M1903', 'M1904', 'M1905', 'M1906', 'M1907', 'M1908', 'M1909']
	coxarthrosis_array = ['M160', 'M161', 'M162', 'M164', 'M165', 'M166', 'M167', 'M169']
	gonarthrosis_array = ['M170', 'M171', 'M172', 'M173', 'M174', 'M175', 'M179']
	arthritis_array = coxarthrosis_array + gonarthrosis_array + rheumatoid_arthritis_array + other_athrosis_array
	#file2 = df.loc[df["41202-0.0"] == 'M161']
	#file2 = df.loc[df['eid'] == 1400897]
	file2 = df.loc[(df['41202-0.0'].isnull()) & (df['41202-0.1'].isnull()) & (df['41202-0.2'].isnull()) & (df['41202-0.3'].isnull()) & (df['41202-0.4'].isnull()) & (df['41202-0.5'].isnull()) & (df['41202-0.6'].isnull()) & (df['41202-0.7'].isnull()) & (df['41202-0.8'].isnull()) & (df['41202-0.9'].isnull()) & (df['41202-0.10'].isnull()) & (df['20002-0.0'].isnull()) & (df['20002-0.1'].isnull()) & (df['20002-0.2'].isnull()) & (df['20002-0.3'].isnull()) & (df['20002-0.4'].isnull()) & (df['20002-0.5'].isnull()) & (df['20002-0.6'].isnull()) & (df['20002-0.7'].isnull()) & (df['20002-0.8'].isnull()) & (df['20002-0.9'].isnull()) & (df['20002-0.10'].isnull())]
	file2.to_csv('control_allrecords.csv', index =False)

#convert UKB ID to regeneron ID didnt work
def convert_IDs():
	df = pd.read_csv("id_and_medical.csv", low_memory = False)
	df2 = pd.read_csv("UKB500K_sampleID_RGCPID.csv")

	df.insert(1, 'rgcpID', np.nan)

	for idx, row1 in df.iterrows():
		for idx, row2 in df2.iterrows():
			if row1.eid == row2.eid:
				df.set_value(idx, 'rgcpID', row2.rgcpID) #has warning that set value may be removed at some point
	df.to_csv("OA_RA_withIDs.csv", index = False)

#convert UKB ID to regeneron ID worked
def convert_IDs_2():
	df = pd.read_csv("clinical_columns.csv", low_memory = False)
	df2 = pd.read_csv("UKB500K_sampleID_RGCPID.csv")

	result = pd.merge(df, df2, on = ['eid'])
	
	#result = pd.concat([df, df2], axis = 1, join = 'inner')

	#result = df2.join(df, how="left")

	result.to_csv("clinical_columns_regID.csv", index = False)

#add IDPs
def IDPs_OA_RA():
	df = pd.read_csv("all_OA.csv", low_memory = False)
	df2 = pd.read_csv("IDPs_table2.csv")

	result = pd.merge(df, df2, on = ['FID'])

	result.to_csv("all_OA_wIDPs.csv", index = False)

def IDPs_control():
	df = pd.read_csv("control_allrecords.csv")
	df2 = pd.read_csv("IDPs_table2.csv")

	result = pd.merge(df, df2, on = ['FID'])

	result.to_csv("all_control_wIDPs.csv", index = False)

def add_med_column():
	df = pd.read_csv("ukb24295.csv", usecols = ['eid', '41202-0.0', '41202-0.1', '41202-0.2', '41202-0.3', '41202-0.4', '41202-0.5'])
	df2 = pd.read_csv("control_wIDPs.csv")

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv("controls_wmedical.csv", index = False)

def all_OA():
	df = pd.read_csv("OA_selfreport.csv", low_memory = False)
	df2 = pd.read_csv("OA_hospital.csv", low_memory = False)

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_OA.csv", index = False)


def main():
	#with open("ukb24295.csv", 'rb') as f:
		#row_count = sum(1 for line in f)
		#print(row_count)
		#502544
	#seperate_medical()
	#first_1000()
	#find_OA_RA_1000()
	#convert_IDs()
	#convert_IDs_2()
	#first_40000()
	#find_OA_hosp()
	#find_control()
	IDPs_OA_RA()
	IDPs_control()
	#add_med_column()
	#find_OA_self()
	#all_OA()
main()


#add age(year) --> "34-0.0" gender --> "31-0.0 (0 is female, 1 is male), standing height --> "50-0.0", waist circumfirance --> "48-0.0", weight --> "3160-0.0", handedness --> "1707-0.0"
#identify 60 people with 


#in control group remove all types of pain
#keep people will OA and any form of 3+ month pain

