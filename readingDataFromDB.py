import pypyodbc
import pandas as pd
import time

start = time.time()
cnxn = pypyodbc.connect("Driver={SQL Server};"
                        "Server=10.17.162.1;"
                        "Database=CA_UIM_CHOSERVER1;"
                        "uid=sa;pwd=interOP@123sys")
print('connected')

# cursor = cnxn.cursor()
sql = pd.read_sql_query('select * from cm_nimbus_robot',cnxn)
# cursor.execute('''select * from cm_nimbus_robot''')
# row =cursor.fetchall()
# cnxn.commit()
# cursor.close()
# cnxn.close()
# for i in row:
#     print(i)

print(sql)
print('Scrip[t has taken : ', (time.time() - start) / 60, 'Minutes............')
