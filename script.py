import smtplib
from getpass import getpass


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
senderemail = input("Type your email and press enter: ")
password = getpass("Type your password and press enter: ")
try:
    server.login(senderemail, password)
except:
    print("Error -- incorrect password or invalid email address. Please try again!")
    exit()

file = open('message.txt', mode = 'r', encoding = 'utf-8-sig')
message = file.read()
file.close()

subject = "A plea from a concerned community member regarding the 2020-2021 proposed budget" 
body = "Subject: {}\n\n{}".format(subject, message)

file = open('recipients.txt', mode = 'r', encoding = 'utf-8-sig')
emails = file.readlines()
file.close()

for email in emails:
    server.sendmail(senderemail, email.strip(), body)

server.quit()