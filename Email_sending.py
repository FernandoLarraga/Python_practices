import smtplib
import ssl 
from email.message import EmailMessage

subject = "Email from Python"
body = "This is a test email from Python!"
sender_email = "pythonpruebas97@gmail.com"
receiver_email = "fernandolarraga97@gmail.com"
password = input("Put here your password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

'''Ya no se permite por la cuenta de google mandar mensajes con este script, ya que no se admite el acceso solo con 
contraseña y usuario, se debe de utilizar otro método de autenticación'''
