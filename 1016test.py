import psycopg2
import pandas as pd
import numpy as np
conn = psycopg2.connect(database="sdms_emea_base",user="a_appconnect",password="ES49#uqj",
                        host="10.122.46.75",port="5432")
cur=conn.cursor()
cur.execute('SELECT * FROM "base_cpo_calculation_2019Q3"')
calcu_result=cur.fetchall()
df=pd.DataFrame(calcu_result)
print(df.describe())
print(df.shape)

