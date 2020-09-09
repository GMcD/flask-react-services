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
        first_name = data['first_name']
        last_name = data['last_name']
        message = data['message']
        duration = int(data['duration'])
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
