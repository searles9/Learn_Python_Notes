# Emails with Python
***
***
# Intro
* this is reliant on - local admin privs, the internet and your email
# Sending emails with Python
* the smtplib library allows you to manually go through the steps of creating and sending an email in Python
#### steps
* connect to an email server
* confirm the connection
* set a protocal
* login
* send the message

#### popular smtp domain names
* gmail: smtp.gmail.com
* yahoo mail:  	smtp.mail.yahoo.com
* outlook.com:   smtp-mail.outlook.com
* at&t:  smpt.mail.att.net (Use port 465)
* verizon: smtp.verizon.net (Use port 465) 
* comcast: smtp.comcast.net

#### sending email
* import
```
import smtplib
```
* create the smtp object for a server
```
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
```
* run the ehlo() command which establishes the connection
```
smtp_object.ehlo()
# it should return 250 as the first value in a tuple if sucessful 
```
* initiate tsl if using port 587
```
smtp_object.starttls()
```
* get the email password - using getpass so its not hardcoded (for gmail you need an app password)
```
import getpass
email = getpass.getpass("Enter your email: ")
password = getpass.getpass("Enter your password: ")
```
* login with the email and pass
```
smtp_object.login(email,password)
```
* send email 
* notice how in the message portion you have the new line character - that indicates for example that the subject text has stopped
```
from_address = getpass.getpass("Enter your email: ")
to_address = getpass.getpass("Enter the email of the recipient: ")
subject = input("Enter the subject line: ")
message = input("Type out the message you want to send: ")
msg = "Subject: " + subject + '\n' + message
smtp_object.sendmail(from_address,to_address,msg)

# it should return an empty dictionary is sucessful 
```
* close the email session
```
smtp_object.quit()
```

***
***
# Receiving Emails with Python 
* you can read and search recived emails using the imaplib library. You can also use the built in email library
* imaplib: https://docs.python.org/3/library/imaplib.html

```
import imaplib
M = imaplib.IMAP4_SSL('imap.gmail.com')
import getpass
user = input("Enter your email: ")
# app password if you are a gmail user
password = getpass.getpass("Enter your password: ")
M.login(user,password)
```
* show email folders:
```
M.list()
```
* ex of connecting to the inbox:
```
# Connect to your inbox
M.select("inbox")
```
* use this if you get an error saying limit was reached - there are often size limits ..this is how you change the limit :
```
imaplib._MAXLINE = 10000000
```
* to seach you have to use the special imap syntax - notice the ```'SUBJECT "text"'```
```
typ ,data = M.search(None,'SUBJECT "this is a test email for python"')

# returns:
# typ returns ok
# data returns a unique ID like this [b'28298']
```
* data will be a list of unique ids
```
# typ, data = M.fetch(data[0],"(RFC822)")
result, email_data = M.fetch(data[0],"(RFC822)")
raw_email = email_data[0][1]
raw_email_string = raw_email.decode('utf-8')
```
* you can use the build in email library to parse the raw string
```
import email
email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():
    if part.get_content_type() == "text/plain":
        body = part.get_payload(decode=True)
        print(body)
```