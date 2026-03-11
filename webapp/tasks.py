from celery import shared_task


@shared_task()
def print_text():
    print('Hello World')


@shared_task(bind=True, autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={'max_retries': 10})
def send_email_task(self, user_id, context: dict):
    print('Sending email...')