import pandas as pd

tables = pd.read_html("https://www.statsf1.com/en/statistiques/pilote/victoire/nombre.aspx", attrs = {'id': 'ctl00_CPH_Main_GV_Stats'})


print(tables)
