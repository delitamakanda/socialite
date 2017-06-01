from threading import Thread
from flask.ext.mail import Message
from flask import render_template, current_app
from . import mail
from .decorators import async


@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(app.config['MAIL_SUBJECT_PREFIX'] + subject, sender=app.config['MAIL_SENDER'], recipients=[to])
    msg.body = render_template(template + '.txt', **kwargs)
    msg.html = render_template(template + '.html', **kwargs)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
    return thr
    
    
def follower_notification(followed, follower):
    send_email("Socialite %s is now following you!" % follower.nickname, current_app.config['ADMIN'], [followed.email], render_template("mail/follower_email.txt"), render_template("mail/follower_email.html"))
