import random
import smtplib  #simple message transfer protocol library

server=smtplib.SMTP('smtp.gmail.com',587) # creating gmail server (server code '587')
server.starttls() #security transfer layered security
server.login('zainulkhan032@gmail.com','isidrnoawvulsnpd')
b = ''.join([str(random.randint(0,9)) for i in range(4)]) # generates '4448' OTP GENERATE
msg='HELLO ,YOUR OTP IS '+str(b)
server.sendmail('zainulkhan032@gmail.com','zainulcharmingboy@gmail.com',msg)
server.quit()

b1 = str(input("Enter the OTP for verification\n"))

def check_otp():
   if(b1==b):
    return True
           
   else:
        return False

if(check_otp()):
    server=smtplib.SMTP('smtp.gmail.com',587) # creating gmail server (server code '587')
    server.starttls() #security transfer layered security
    server.login('zainulkhan032@gmail.com','isidrnoawvulsnpd')
    msg='Congratulation you have successfully clear the OTP test'
    server.sendmail('zainulkhan032@gmail.com','zainulcharmingboy@gmail.com',msg)
    server.quit()
else:
    server=smtplib.SMTP('smtp.gmail.com',587) # creating gmail server (server code '587')
    server.starttls() #security transfer layered security
    server.login('zainulkhan032@gmail.com','isidrnoawvulsnpd')
    msg='Sorry you entered wrong OTP'
    server.sendmail('zainulkhan032@gmail.com','zainulcharmingboy@gmail.com',msg)
    server.quit()
      

