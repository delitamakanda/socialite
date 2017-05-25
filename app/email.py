from flask.ext.mail import Message
from config import config

config['FLASKY_MAIL_SUBJECT_PREFIX'] = 'Socialite'
config['FLASKY_MAIL_SENDER'] = 'Socialite Team <delita.makanda@gmail.com>'

def send_email(to, subject, template, **kwargs):
    msg = Message(config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject, sender=config['FLASKY_MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    mail.send(msg)
