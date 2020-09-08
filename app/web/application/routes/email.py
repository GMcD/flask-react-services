from smtplib import SMTPException

from flask import flash, render_template, request, redirect, url_for
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

@app.route('/email', methods=['GET', 'POST'])
def email():
    """
        Email form
    """
    if request.method == 'GET':
        return render_template('email.html')

    elif request.method == 'POST':
        data = request.form
        email = data['email']
        first_name = data['first_name']
        last_name = data['last_name']
        message = data['message']
        duration = data['duration']
        duration_unit = data['duration_unit']

        if duration_unit == 'minutes':
            duration *= 60
        elif duration_unit == 'hours':
            duration *= 3600
        elif duration_unit == 'days':
            duration *= 86400

        send_mail.apply_async(args=[data], countdown=duration)
        flash(f"Email will be sent to {data['email']} in {request.form['duration']} {duration_unit}")

        return redirect(url_for('index'))
