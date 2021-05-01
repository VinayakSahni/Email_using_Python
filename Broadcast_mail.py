#We are going to use SMTP(Simple Message Transfer Protocol) Library for sending the mail through a medium
#Also used to transfer resources from one server to another
import smtplib
#getting a password from user, it is encrypted & no information of pswd is written over command line, not even the stars!
import getpass
#To contain all the information in a message format we use mimetext like subject,from,to etc
from email.mime.text import MIMEText
#enable the third party access from gmail account settings


def send_email():
    sender_Address="***********@gmail.com"  
    #getting a pswd from user without showing in the cmd and also encryoting it 
    password=getpass.getpass()
    subject='Sending from Python'
    message='''
        This message was sent using python without any use of email

        With Regards
        *******

    '''

    #Server Intialisation
    #host->smtp.gmail.com, port->587 for gmail  server will get intiated
    server=smtplib.SMTP('smtp.gmail.com', 587)
    #starting the server, its just like TLS handshake i.e. -> During a TLS handshake, the two communicating sides exchange messages to acknowledge each other, verify each other, establish the encryption algorithms they will use, and agree on session keys.
    server.starttls()
    #login into ur server
    server.login(sender_Address, password)
    print('Login successful !')

    #Drafting my message body
    msg=MIMEText(message)
    msg['Subject']=subject
    msg['From']=sender_Address
    msg['To']='Recievers address*****'
    #specifying the importance of message
    msg.set_param('importance','high value')

    #ONLY CHANGE
    #ONLY CHANGE
    #ONLY CHANGE
    #Pass an array of mails to whom the mail is to be sent !!!!!!!!
    recipient=['Recievers address*****(1)','Recievers address*****(2)']

    #sending the mail
    server.sendmail(sender_Address, recipient, msg.as_string())
    print('Email has been sent !')
    server.quit()

send_email()




'''                           OR THE RECIPIENTS CAN BE GIVEN IN THIS WAY  (IDEAL WAY)      ''''

# #We are going to use SMTP(Simple Message Transfer Protocol) Library for sending the mail through a medium
# #Also used to transfer resources from one server to another
# import smtplib
# #getting a password from user, it is encrypted & no information of pswd is written over command line, not even the stars!
# import getpass
# #To contain all the information in a message format we use mimetext like subject,from,to etc
# from email.mime.text import MIMEText
# #enable the third party access from gmail account settings


# def send_email():
#     sender_Address="***********@gmail.com"  
#     #getting a pswd from user without showing in the cmd and also encryoting it 
#     password=getpass.getpass()
#     subject='Sending from Python'
#     message='''
#         This message was sent using python without any use of email

#         With Regards
#         *******

#     '''

#     #Server Intialisation
#     #host->smtp.gmail.com, port->587  server will get intiated
#     server=smtplib.SMTP('smtp.gmail.com', 587)
#     #starting the server, its just like TLS handshake i.e. -> During a TLS handshake, the two communicating sides exchange messages to acknowledge each other, verify each other, establish the encryption algorithms they will use, and agree on session keys.
#     server.starttls()
#     #login into ur server
#     server.login(sender_Address, password)
#     print('Login successful !')

'''    CHANGE
    CHANGE   '''
#     recipient=['Recievers address*****(1)','Recievers address*****(2)']


#     #Drafting my message body
#     msg=MIMEText(message)
#     msg['Subject']=subject
#     msg['From']=sender_Address

'''  CHANGE OF MSG['TO'] using ",".join(recipient)'''

#     msg['To']=",".join(recipient)
#     #specifying the importance of message
#     msg.set_param('importance','high value')

#     #ONLY CHANGE
#     #ONLY CHANGE
#     #ONLY CHANGE
#     #Pass an array of mails to whom the mail is to be sent !!!!!!!!

#     #sending the mail
#     server.sendmail(sender_Address, recipient, msg.as_string())
#     print('Email has been sent !')
#     server.quit()

# send_email()