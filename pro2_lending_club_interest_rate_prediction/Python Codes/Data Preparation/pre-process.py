import pandas as pd
import random

reader1 = pd.read_csv('test_data.csv',error_bad_lines=False,encoding = "utf-8")

reader1 = reader1[reader1['title'].isnull()==False]
reader1 = reader1[reader1['revol_util'].isnull()==False]
reader1 = reader1[reader1['last_pymnt_d'].isnull()==False]
reader1 = reader1[reader1['dti_joint'].isnull()==False]
reader1 = reader1[reader1['open_acc_6m'].isnull()==False]
reader1 = reader1[reader1['num_tl_120dpd_2m'].isnull()==False]

print(reader1['next_pymnt_d'].loc[1:3])

vsj_fill_list = reader1['verification_status_joint'][reader1['verification_status_joint'].isnull().values==True].index.tolist()

for i in vsj_fill_list:
	x = random.randint(1,36732+21833+13880);
	if (x<=36732):
		reader1['verification_status_joint'].at[i] = 'Not Verified';
	elif (x<=36732+21833):		
		reader1['verification_status_joint'].at[i] = 'Source Verified';
	elif (x<=36732+21833+13880):
		reader1['verification_status_joint'].at[i] = 'Verified'

#fill_msr
msr_have_list = reader1['mths_since_rcnt_il'][reader1['mths_since_rcnt_il'].isnull().values==False].index.tolist()
ci = 0
tot_num = 0
for i in msr_have_list:
	ci = ci + 1
	tot_num = tot_num + int(reader1['mths_since_rcnt_il'].at[i])
fill_num = int(tot_num/ci)
reader1['mths_since_rcnt_il'] = reader1['mths_since_rcnt_il'].fillna(fill_num)

#fill_iu
iu_have_list = reader1['il_util'][reader1['il_util'].isnull().values==False].index.tolist()
ci = 0
tot_num = 0
for i in iu_have_list:
	ci = ci + 1
	tot_num = tot_num + int(reader1['il_util'].at[i])
fill_num = int(tot_num/ci)
reader1['il_util'] = reader1['il_util'].fillna(fill_num)

#fill botb
botb_have_list = reader1['bc_open_to_buy'][reader1['bc_open_to_buy'].isnull().values==False].index.tolist()
ci = 0
tot_num = 0
for i in botb_have_list:
	ci = ci + 1
	tot_num = tot_num + int(reader1['bc_open_to_buy'].at[i])
fill_num = int(tot_num/ci)
reader1['bc_open_to_buy'] = reader1['bc_open_to_buy'].fillna(fill_num)

#fill bu
bu_have_list = reader1['bc_util'][reader1['bc_util'].isnull().values==False].index.tolist()
ci = 0
tot_num2 = 0.0
for i in bu_have_list:
	ci = ci + 1
	tot_num2 = tot_num2 + reader1['bc_util'].at[i]
fill_num2 = tot_num2/ci
reader1['bc_util'] = reader1['bc_util'].fillna(fill_num2)

#fill_msoia
msoia_have_list = reader1['mo_sin_old_il_acct'][reader1['mo_sin_old_il_acct'].isnull().values==False].index.tolist()
ci = 0
tot_num = 0
for i in msoia_have_list:
	ci = ci + 1
	tot_num = tot_num + int(reader1['mo_sin_old_il_acct'].at[i])
fill_num = int(tot_num/ci)
reader1['mo_sin_old_il_acct'] = reader1['mo_sin_old_il_acct'].fillna(fill_num)

#fill_msri
msri_have_list = reader1['mths_since_recent_bc'][reader1['mths_since_recent_bc'].isnull().values==False].index.tolist()
ci = 0
tot_num = 0
for i in msri_have_list:
	ci = ci + 1
	tot_num = tot_num + int(reader1['mths_since_recent_bc'].at[i])
fill_num = int(tot_num/ci)
reader1['mths_since_recent_bc'] = reader1['mths_since_recent_bc'].fillna(fill_num)

#fill pbg7
pbg7_have_list = reader1['percent_bc_gt_75'][reader1['percent_bc_gt_75'].isnull().values==False].index.tolist()
ci = 0
tot_num2 = 0.0
for i in pbg7_have_list:
	ci = ci + 1
	tot_num2 = tot_num2 + reader1['percent_bc_gt_75'].at[i]
fill_num2 = tot_num2/ci
reader1['percent_bc_gt_75'] = reader1['percent_bc_gt_75'].fillna(fill_num2)

print(fill_num)

reader1.describe()

dti_mean = reader1["dti"].mean()

reader1["dti"] = reader1["dti"].fillna(dti_mean)

missing = reader1.columns[reader1.isnull().any()].tolist()

print(reader1[missing].isnull().sum())

reader1.to_csv('fillFinishData.csv')