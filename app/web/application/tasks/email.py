from smtplib import SMTPException

from flask import current_app as app
from flask_mail import Message

from web.application import mail, celery

# Send Mail Celery Task
@celery.task
def send_mail(data):
    """
        Function to send emails.
    """
    sender = app.config['MAIL_USERNAME']
    suppressed = 'Not sending' if 'MAIL_SUPPRESS_SEND' in app.config and app.config['MAIL_SUPPRESS_SEND'] else 'Sending'
    msg = Message("Ping!", sender=sender, recipients=[data['email']])
    msg.body = data['message']
    result = "{} email from '{}'".format(suppressed, sender)
    try:
        mail.send(msg)
        app.logger.info(result)
    except SMTPException as e:
        result = "Error {} : {}".format(result, e)
        app.logger.error(result)
    return result
