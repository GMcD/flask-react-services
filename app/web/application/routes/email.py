from flask import flash, render_template, request, redirect, url_for
from flask import current_app as app

from web.application.tasks.email import send_mail

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
        duration = int(data['duration'])
        duration_unit = data['duration_unit']

        flash(f"Email will be sent to {email} in {duration} {duration_unit}")

        if duration_unit == 'minutes':
            data['duration'] *= 60
        elif duration_unit == 'hours':
            data['duration'] *= 3600
        elif duration_unit == 'days':
            data['duration'] *= 86400

        send_mail.apply_async(args=[data], countdown=duration)

        return redirect(url_for('index'))
