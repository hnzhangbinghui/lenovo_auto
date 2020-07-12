#博文地址：https://blog.csdn.net/weixin_33730836/article/details/92096481
#coding:utf-8
import psycopg2
import pandas as pd
import numpy as np
import sys
import xlwt
import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import os.path
sheet_name='report'+time.strftime("%Y-%m-%d")
filename='report'+time.strftime("%Y-%m-%d"+'-'+"%H%M%S")+'.xlsx'
out_path="e:/test/report"+time.strftime("%Y-%m-%d"+'-'+"%H%M%S")+".xlsx"
#路径文件名文件名使用日期来命名，但是文件命名不支持冒号，所以去掉冒号；
cur_path="e:/test"
sql="SELECT * FROM calculation_result_info WHERE program_id='670016283'"
#链接数据库
#def export():
conn = psycopg2.connect(database="sdms_emea_base",user="a_appconnect",password="ES49#uqj",
                        host="10.122.46.75",port="5432")
cur=conn.cursor()
cur.execute(sql)
result=cur.fetchall()
count=cur.rowcount
print("Select "+str(count)+" Records")

fields=cur.description   #数据表的标题
#print(fields)
workbook=xlwt.Workbook(encoding='utf-8')  # 创建excel文档
sheet=workbook.add_sheet(sheet_name,cell_overwrite_ok=True)  #根据sheet_name创建excel文档的sheet
for field in range(0,len(fields)):
    sheet.write(0,field,fields[field][0])   #得到excel的列头的值
    #print(fields[field][0])

#逐行逐列的添加数据
for row in range(1,len(result)+1):
    for col in range(0,len(fields)):
        sheet.write(row,col,u'%s'%result[row-1][col])
workbook.save(out_path)   #按照out_path的格式和路径保存excel表格
#
# _user="binghui.zhang@hand-china.com"
# _pwd='Zbh@911915'
# areceiver="hnzhangbinghui@163.com"
# acc="809665385@qq.com"
# #如名字所示Multipart就是多个部分
# msg=MIMEMultipart()
# msg["Subject"]=u'[DATA Select_'+time.strftime("%Y-%m-%d")+u']'
# msg["From"]=_user
# msg["To"]=areceiver
# msg["CC"]=acc

# def send_email():
#     conn = psycopg2.connect(database="sdms_emea_base", user="a_appconnect", password="ES49#uqj",
#                             host="10.122.46.75", port="5432")
#     cur = conn.cursor()
#     cur.execute(sql)
#     cur.fetchall()
#     count=cur.rowcount
#     #--这是文字部分--
#     content= '''Dear All, \n 附件是每日统计情况,请查收！总计结果数位:'''+ str(count)
#     part=MIMEText(content,'plain','utf-8')
#     msg.attach(part)
#     if count>0:
#         #这是附件部分,xls类型附件
#         print(filename)
#         file_name=r'E:/test/'+filename
#         part=MIMEText(open(file_name,'rb').read(),'base64','gb2312')
#         part["Content-Type"]='application/octet-stream'
#         basename=os.path.basename(file_name)
#         part['Content-Disposition'] = 'attachment; filename=%s' % basename
#         msg.attach(part)
#         s=smtplib.SMTP('mail.ucinbox.com',timeout=120) #链接smtp邮件服务器
#         print("Email send sucessfully")
#         s.close()
#     else:
#         print("nothing to send")
# if __name__=='__main__':
#     export()
#     send_email()













