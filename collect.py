import pandas as pd

years = range(2018, 2019)
gp_names = open("Data/gp_list.txt", "r")

gp_year = '2018'
gp_name = 'australie'

table = pd.read_html("https://www.statsf1.com/en/" +gp_year+ "/" +gp_name+ "/classement.aspx", attrs = {'id': 'ctl00_CPH_Main_GV_Stats'})[0]
print(table)		
for gp_year in years:
	gp_year = str(gp_year)
	print(gp_year)
	for gp_name in gp_names:
		gp_name = str(gp_name)
		print(gp_name)
		table = pd.read_html("https://www.statsf1.com/en/" +gp_year+ "/australie/classement.aspx", attrs = {'id': 'ctl00_CPH_Main_GV_Stats'})[0]
		print(table)		
		with open(''+gp_year+gp_name+'.txt', 'w') as output:
			output.write(table)

#print(table.iloc[0:20,:])
# table = table[1:2,1:2]
# print(table)





