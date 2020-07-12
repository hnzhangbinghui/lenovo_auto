import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
conn = psycopg2.connect(database="sdms_emea_calculation",user="a_appconnect",password="ES49#uqj",
                        host="10.122.46.75",port="5432")
cur=conn.cursor()
engine=create_engine('postgresql://a_appconnect:ES49#uqj@10.122.46.75:5432/sdms_emea_calculation')
cur.execute("SELECT * FROM calculation_result_info WHERE program_id='670016283'")
calcu_result=cur.fetchall()
print(len(calcu_result))
calcu_result_list=[]
for i in range(len(calcu_result)):
    calcu_result_list.append(list(calcu_result[i]))
print(calcu_result_list)
for i in calcu_result_list:
    df=pd.read_sql_query("""SELECT * FROM calculation_result_info WHERE program_id='670016283';""",con=engine)
    df.to_excel('calcu_result283.xlsx')


