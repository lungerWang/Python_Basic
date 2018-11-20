from email.mime.text import MIMEText
msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
from_addr = '836414757@qq.com'
pwd = 'wbl2123123321'
to_addr = '13823208010@163.com'
smtp_server = 'smtp.qq.com'
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()