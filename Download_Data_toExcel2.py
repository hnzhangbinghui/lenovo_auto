import psycopg2
import pandas as pd
import numpy as np
from sqlalchemy import create_engine
conn = psycopg2.connect(database="sdms_emea_base",user="a_appconnect",password="ES49#uqj",
                        host="10.122.46.75",port="5432")

with conn:
    cur=conn.cursor()
    cur.execute("SELECT * FROM base_nomination")
    rows=cur.fetchall()
    t=pd.DataFrame(rows)
    t.to_excel('nomination_data.xlsx')



