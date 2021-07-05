from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone

from .models import Job_status

#runs every midnight
@periodic_task(run_every=crontab(minute=0, hour=0))
def delete_old_foos():
    # Query all the expired date in our database
    userMedia = Job_status.objects.all()
    # Or get a specific user id to delete their file
    # Iterate through them
    for file in userMedia:
        if file.expiration_date is not None and file.expiration_date < timezone.now():
            file.delete()

@periodic_task(run_every=15)
def sum():
    print('hey there, people', 'is here')
