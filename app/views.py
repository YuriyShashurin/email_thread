from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.core.mail import send_mail
from django.utils import timezone
import threading

from app.models import Mail
# Create your views here.


def worker(mail_pk,subject,text,sender,to):
    query = Mail.objects.get(pk=mail_pk)
    send_mail(subject,text,sender,to,fail_silently=False)
    query.status = True
    query.sent_time = timezone.now()
    query.save()
    return True

class CreateMailView(CreateView):
    model = Mail
    template_name = 'index.html'
    success_url = 'mails/'
    fields = ['subject', 'text', 'sender', 'recipient', 'interval']


    def form_valid(self, form):
        if self.request.POST:
            self.object = form.save()
            mail_pk = self.object.pk
            subject = form.cleaned_data['subject']
            text = form.cleaned_data['text']
            recipient = form.cleaned_data['recipient']
            to = [recipient]
            sender = form.cleaned_data['sender']
            interval = form.cleaned_data['interval']
            t = threading.Timer(interval, worker, args=(mail_pk,subject,text,sender,to, ))
            a = t.start()
            if a:
                t.join()
        return super().form_valid(form)

class ListMailView(ListView):
    model = Mail
    template_name = 'mail_list.html'

    def get_queryset(self):
        last_ten = Mail.objects.all().order_by('-id')[:10]
        return last_ten