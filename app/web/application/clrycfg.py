# List of modules to import when the Celery worker starts.
imports = ('web.application.tasks',)

from celery.schedules import crontab

beat_schedule = {

        # test celery beat scheduling...
        # 'send_email' : {
        #     'task'      :'web.application.tasks.email.send_mail',
        #     'schedule'  : crontab(minute='*/2'),
        #     'args'      : ( {'email' : 'gary.macdonald@projectscapa.com', 'subject' : 'Cron', 'message' : 'Job'}, )
        # },
    }
