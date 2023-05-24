from decouple import config
from email.message import EmailMessage
import ssl 
import smtplib




emailEmisor = config('EMAIL_EMISOR')
emailConsena = config('EMAIL_PASSWORD')
emailReceptor = input('Agrega al receptor: example@correo.com: \n')

asunto = input("Agrega el asunto para tu correo electronico: \n")
cuerpo = input("Agrega el cuerpo del correo: \n")

em = EmailMessage()
em['From'] = emailEmisor
em['To'] = emailReceptor
em['Subject'] = asunto
em.set_content(cuerpo)

contexto = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=contexto) as smtp:
    smtp.login(emailEmisor,emailConsena)        
    smtp.sendmail(emailEmisor, emailReceptor, em.as_string())

