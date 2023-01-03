from email.message import EmailMessage # set email class for email structure
import ssl # safeguards sensitive data being sent between 2 systems
import smtplib # sends email via SMTP connection

email_sender = 'emailbinsender221@gmail.com'
email_password = input("Enter app password: ")

email_receiver = 'jiced91966@cmeinbox.com' # using temp mail

subject = "Hello there!"
body = """
Hello there I have sent you a message!
"""

em = EmailMessage() # instantiate EmailMessage()

# defining elements of EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context() # creates secure SSL context

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp: # sets up SMTP server address (gmail) with port number and ssl
    smtp.login(email_sender, email_password) # logs into email id
    smtp.sendmail(email_sender, email_receiver, em.as_string()) # sends mail
