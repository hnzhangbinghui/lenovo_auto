#coding:utf-8
# import smtplib
# smtpObj=smtplib.SMTP([127.0.0.1 [3306,[local_hostname]]])
'''
参数解析：
1、host：SMTP服务器主机，你可以指定主机的IP地址或者域名：ziqiangxuetang.com，这个是可选参数
2、port：如果你提供了host参数，你需要指定SMTP服务使用的端口号，一般情况下SMTP端口号是25；
3、local_hostname：如果SMTP在你的本机上，你只需要指定服务器地址为localhost即可；
'''
#python SMTP对象使用sendmail方法发送邮件：语法如下：
#smtpObj.sendmail(from_addr="hnzhangbinghui@163.com",to_addrs="809665385@qq.com",msg[,mail_options="",
#rcpt_options=""])
'''
参数解析：
1、from_addr，邮件发送者地址
2、to_addrs，字符串列表，邮件发送地址；
3、msg，发送消息，这里要注意一下第三个参数，msg是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意msg的格式。这个格式就是smtp协议中定义的格式。

'''

import smtplib
from email.mime.text import MIMEText #email用于构建邮件内容
from email.header import Header  #用于构建邮件头
#发信方的信息：发信邮箱，qq邮箱授权码
from_addr="809665385@qq.com"
password='ujgzewqwraogbfbd'
#收信方邮箱
to_addr="hnzhangbinghui@163.com"
#发信服务器
smtp_server='smtp.qq.com'
#邮箱正文内容，第一个参数为内容，第二个参数为格式（plain为纯文本），第三个参数为编码
msg=MIMEText("哈喽，到哪里啦，我等会去接你，老地方见！！",'plain','utf-8')
#邮件头信息
msg['From']=Header(from_addr)
msg['To']=Header(to_addr)
msg['Subject']=Header("python test20191103")
#开启发信服务，这里使用的是加密传输
#smtplib.SMTP_SSL(host='smtp.qq.com').connect(host='smtp.qq.com',port=465)
server=smtplib.SMTP_SSL(smtp_server)
server.connect(smtp_server,465)
#登录发信邮箱
server.login(from_addr,password)
#发送邮件
server.sendmail(from_addr,to_addr,msg.as_string())

#关闭服务器
#server.quit()


