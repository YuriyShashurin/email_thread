from django.db import models
from django.core.mail import send_mail
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Mail (models.Model):
    subject = models.CharField(max_length=150, verbose_name='Тема письма')
    text = models.TextField(verbose_name='Текст сообщения')
    sender = models.EmailField(verbose_name='Адрес отправителя', default=settings.EMAIL_HOST_USER)
    recipient = models.EmailField(verbose_name='Адрес получателя')
    interval = models.SmallIntegerField(verbose_name='Интервал отправки')
    status = models.BooleanField(default=False,verbose_name='Статус отправки')
    sent_time = models.DateTimeField(null=True, blank=True)

