# builtins
from smtplib import SMTPAuthenticationError
import datetime

# dependencies
from yagmail import SMTP

_ADMIN_MAIL = 'jaimelesfraisesbleues@gmail.com'

def send_mail(name: str, mail: str, subject: str, body: str) -> bool:
    current = datetime.datetime.now()
    yag = SMTP(_ADMIN_MAIL, "oxvdwydiiunywnou")
    try:
        recap = f"Votre message a bien été envoyé. Voici un récapitulatif :\nVotre nom : {name}\nVotre message : \n{body}\n\nEnvoyé le {current.day}/{current.month}/{current.year} à {current.hour}:{current.minute}"
        message = f'{name} ({mail})\n\n{body}\n\nEnvoyé le {current.day}/{current.month}/{current.year} à {current.hour}:{current.minute}'
        yag.send(mail, subject, recap)
        yag.send(_ADMIN_MAIL, subject, message)
        return True
    except SMTPAuthenticationError:
        print('Unable to login !')
        return False