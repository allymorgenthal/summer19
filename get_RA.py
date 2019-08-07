import pandas as pd

def find_RA():
	df = pd.read_csv('clinical_columns_regID.csv')

	otherRA_hosp = ['M0680', 'M0681', 'M0682', 'M0685', 'M0686', 'M0687', 'M0688', 'M0689', 'M0690', 'M0691', 'M0692', 'M0693', 'M0694', 'M0695', 'M0696', 'M0697', 'M0698', 'M0699']
	RA_self = ['1464']
	seroposRA_hosp = ['M0580', 'M0582', 'M0583', 'M0584', 'M0586', 'M0587', 'M0588', 'M0589', 'M0590', 'M0591', 'M0592', 'M0593', 'M0594', 'M0595', 'M0596', 'M0597', 'M0598', 'M0599']
	seronegRA_hosp = ['M0600', 'M0601', 'M0602', 'M0603', 'M0604', 'M0605', 'M0606', 'M0607', 'M0608', 'M0609']


	self_report_array = RA_self 
	hosp_record_array = otherRA_hosp + seroposRA_hosp + seronegRA_hosp

	file2 = df.loc[(df['20002-0.0'].isin(self_report_array)) | (df['20002-0.1'].isin(self_report_array)) | (df['20002-0.2'].isin(self_report_array)) | (df['20002-0.3'].isin(self_report_array)) | (df['20002-0.4'].isin(self_report_array)) | (df['20002-0.5'].isin(self_report_array)) | (df['20002-0.6'].isin(self_report_array)) | (df['20002-0.7'].isin(self_report_array)) | (df['20002-0.8'].isin(self_report_array)) | (df['20002-0.9'].isin(self_report_array)) | (df['20002-0.10'].isin(self_report_array))]
	file3 = df.loc[(df['41202-0.0'].isin(hosp_record_array)) | (df['41202-0.1'].isin(hosp_record_array)) | (df['41202-0.2'].isin(hosp_record_array)) | (df['41202-0.3'].isin(hosp_record_array)) | (df['41202-0.4'].isin(hosp_record_array)) | (df['41202-0.5'].isin(hosp_record_array)) | (df['41202-0.6'].isin(hosp_record_array)) | (df['41202-0.7'].isin(hosp_record_array)) | (df['41202-0.8'].isin(hosp_record_array)) | (df['41202-0.9'].isin(hosp_record_array)) | (df['41202-0.10'].isin(hosp_record_array))] 

	file2.to_csv('self_report_RA.csv', index = False)
	file3.to_csv('hosp_record_RA.csv', index = False)

def combine_RA():
	df = pd.read_csv("self_report_RA.csv")
	df2 = pd.read_csv("hosp_record_RA.csv")

	result = pd.concat([df, df2]).drop_duplicates().reset_index(drop=True)

	result.to_csv("all_RA_pain.csv", index = False)

def three_mon_check():
	df = pd.read_csv('yes_pain.csv')
	df2 = pd.read_csv('all_RA_pain.csv')

	result = pd.merge(df, df2, on = ['eid'])

	result.to_csv('RA_3mon.csv', index = False)

def no_cent_pain_check():
	df = pd.read_csv("all_central_pain.csv", low_memory = False)
	df2 = pd.read_csv("RA_3mon.csv", low_memory = False)

	result = df2[~df2.eid.isin(df.eid.values)]

	result.to_csv('RA_3mon_nocent.csv', index = False)

def main():
	#find_RA()
	#combine_RA()
	#three_mon_check()
	no_cent_pain_check()
main()