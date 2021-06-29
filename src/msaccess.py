# import pyodbc
 
# # データベースに接続します
# conn_str = (
#     r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
#     r'DBQ=/Users/znatz/Projects/Python/fastapi_msaccess/src/Burdata.mdb;'
#     )
# conn = pyodbc.connect(conn_str)
# cursor = conn.cursor()
 
# # データベースに含まれるテーブルを取得します
# for table_info in cursor.tables(tableType='TABLE'):
#     print(table_info.table_name)
 
# # データベースの接続を閉じます
# cursor.close()
# conn.close()

import pandas_access as mdb

db_filename = 'Burdata.mdb'

# Listing the tables.
# for tbl in mdb.list_tables(db_filename):
#   print(tbl)

# Read a small table.
df = mdb.read_table(db_filename, "Burdata")
print(df.to_html())