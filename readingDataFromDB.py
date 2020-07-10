import pypyodbc
import matplotlib.pyplot as plt
import pandas as pd
import time
import csv

start = time.time()
cnxn = pypyodbc.connect("Driver={SQL Server};"
                        "Server=10.17.162.1;"
                        "Database=CA_UIM_CHOSERVER1;"
                        "uid=sa;pwd=interOP@123sys")
# print('connected')


sql1 = pd.read_sql_query('''select r_table from s_qos_data where probe = 'cdm' and qos like '%QOS_MEMORY_PERC_USAGE%' and robot like '%server%' ''',cnxn)
sql2 = pd.read_sql_query('''select table_id from s_qos_data where probe = 'cdm' and qos like '%QOS_MEMORY_PERC_USAGE%' and robot like '%server%' ''',cnxn)

l = sql1['r_table']
l1 = sql2['table_id']
rn_table = [l[0], l1[0]]
# print(rn_table)
metric_query = pd.read_sql_query(''' select convert(varchar(20),sampletime,106)as sampletime,samplevalue
 from {} where table_id = {} and sampletime >= DATEADD(hh,-10,getdate())'''.format(rn_table[0],rn_table[1]),cnxn)
print(metric_query)
metric_query.to_csv('cdm.csv', index=False)
cnxn.close()

x=[]
y=[]

with open('cdm.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(str(row[1]))


plt.plot(x,y, marker='o')

plt.title('QOS_MEMORY_PERC_USAGE')

plt.xlabel('Sample Value')
plt.ylabel('Sample Time')

plt.show()
print('Script has taken : ', (time.time() - start) / 60, 'Minutes............')
