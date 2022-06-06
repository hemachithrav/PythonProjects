# Python Project_1( Send Email to Gmail)
#Import Library
import smtplib
server= smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('hcvdemo@gmail.com','qjipqxzgevezkebt')
server.sendmail('hcvdemo@gmail.com','hemachithra31011999@gmail.com','Mail Sent by Python code Project')
print('Mail Sent')