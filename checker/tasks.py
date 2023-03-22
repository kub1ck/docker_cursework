import subprocess
from celery import shared_task
from django.core.mail import send_mail

from cw_docker import settings
from .models import File, FileStatus, Logs


@shared_task
def check_file():
    files = File.objects.filter(status__in=['new', 'updated'])

    for file in files:
        log_text = subprocess.run(['flake8', file.file.path], stdout=subprocess.PIPE).stdout.decode('utf-8')

        try:
            log = Logs.objects.get(file=file)
            log.info = log_text
            log.save()

        except:
            Logs.objects.create(file=file, info=log_text)

        file.status = FileStatus.VERIFIED
        file.save()

        send_email.delay(file.id)


@shared_task
def send_email(pk):
    log = Logs.objects.get(file_id=pk)
    log.send_mail = 1
    log.save()

    send_mail(
        subject='Файл проверен',
        message=log.info,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[log.file.owner.email]
    )
