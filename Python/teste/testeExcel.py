
import pyodbc 
import pandas as pd
import numpy as np

conn_str = (
    r"DRIVER={Microsoft Excel Driver (*.xls)};"
    r"DBQ=C:\Users\Jorge Custanari\desktop\oi.xls;"
    )
cnxn = pyodbc.connect(conn_str, autocommit=True)
query = cnxn.cursor()

query.execute("""
        SELECT 
            Nome
        FROM 
            `Plan1$`

""")
rows = query.fetchall()
print(rows)
# for row in rows:
#     t = row
#     print(t)