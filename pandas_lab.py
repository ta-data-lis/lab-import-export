import pandas as pd

#CSV
cols = ['time', 'rad_flow', 'fpv_close', 'fpv_open', 'high', 'bypass', 'bpv_close', 'bpv_open', 'class']
tst_url ="https://archive.ics.uci.edu/ml/machine-learning-databases/statlog/shuttle/shuttle.tst"
shuttle_data=pd.read_csv(tst_url, sep=' ', names =cols )
print(shuttle_data)

shuttle_data.to_csv('/Users/guillaumeaubert/Documents/Ironhack/Module1/Week2/Day3_Pandas/lab-import-export/your-code/shuttle_data.csv',sep=',',index=False)

#Excel
excel_path='/Users/guillaumeaubert/Documents/Ironhack/Module1/Week2/Day3_Pandas/lab-import-export/your-code/astronauts.xls'

astronaute=pd.read_excel(excel_path)

astronaute.head()
pd.value_counts(astronaute['Undergraduate Major'])
print(pd.value_counts(astronaute['Undergraduate Major']))

astronaute.to_csv('/Users/guillaumeaubert/Documents/Ironhack/Module1/Week2/Day3_Pandas/lab-import-export/your-code/astronaute.csv',sep='    ',index=False)

