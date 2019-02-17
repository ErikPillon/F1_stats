import sys
import datetime as dt

gp_year = []

if len(sys.argv)<3:	
	today = dt.date.today()
	gp_year = today.strftime('%Y')
		
gp_name = sys.argv[1]

print(gp_name)
print(gp_year)

url = 'https://www.statsf1.com/en/'+gp_year+'/'+gp_name+'/classement.aspx'






