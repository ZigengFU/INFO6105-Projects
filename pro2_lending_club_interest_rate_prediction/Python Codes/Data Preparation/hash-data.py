import pandas as pd
import numpy as np

reader1 = pd.read_csv('autoFeatureData.csv',error_bad_lines=False,encoding = "utf-8")


#hash grade
char_list = ['A','B','C','D','E','F','G']
ci = 0
for ch in char_list:
	ci = ci + 1
	change_list=reader1['grade'][reader1['grade']==ch].index.tolist()
	for i in change_list:
		reader1['grade'].at[i] = ci;
	
char_list = [' 60 months',' 36 months']
int_list = [60,36]
ci = 0
for ch in char_list:
	ci = ci + 1
	change_list=reader1['term'][reader1['term']==ch].index.tolist()
	for i in change_list:
		reader1['term'].at[i] = int_list[ci-1];

char_list = ['Verified','Source Verified']
ci = 0
for ch in char_list:
	ci = ci + 1
	change_list=reader1['MODE(person.verification_status)'][reader1['MODE(person.verification_status)']==ch].index.tolist()
	for i in change_list:
		reader1['MODE(person.verification_status)'].at[i] = ci-1;
		

#reader1['revol_util'] = reader1['revol_util'].map(lambda x: x*100)
		
reader1.dropna(axis=0, how='any', inplace=True)

#reader1['total_il_high_credit_limit'] = reader1['total_il_high_credit_limit'].replace([954503,0],int(reader1['total_il_high_credit_limit'].mean()))
#reader1['total_bc_limit'] = reader1['total_bc_limit'].replace([569500,471400,0],int(reader1['total_bc_limit'].mean()))
#reader1['total_bal_ex_mort'] = reader1['total_bal_ex_mort'].replace([1256846,0],int(reader1['total_bal_ex_mort'].mean()))
#reader1['tot_hi_cred_lim'] = reader1['tot_hi_cred_lim'].replace([3429816,100],int(reader1['tot_hi_cred_lim'].mean()))

reader1.to_csv('autoFeatureloadHashFinishData.csv')

reader1.describe().astype(np.int64).to_csv('info.csv')

