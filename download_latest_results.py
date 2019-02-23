import sys
import datetime as dt
import pandas as pd
import numpy
from numpy import array

gp_name = sys.argv[1]

if len(sys.argv)<3:	
	today = dt.date.today()
	gp_year = today.strftime('%Y')
else:
	gp_year = sys.argv[2] 
		
table = pd.read_html("https://www.statsf1.com/en/" +gp_year+ "/" +gp_name+ "/classement.aspx", attrs = {'id': 'ctl00_CPH_Main_GV_Stats'})[0]

# print(table.shape)
print(table.iloc[0:20,:])
# table = table[1:2,1:2]
# print(table)
file_output = ['data_'+gp_year+'_'+gp_name+'.csv']
pd.to_csv(file_output)




