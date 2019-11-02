from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from .forms import FeedBackForm


class FeedBackView(View):

    def post(self, request):
        if request.method == 'POST':
            form = FeedBackForm(request.POST)
            if form.is_valid():
                form.save()

                subject = 'Новая заявка с сайта'
                from_email = 'alex23_95@mail.ru'
                message = 'Новая заявка с сайта \r\n \r\n'
                message += form.cleaned_data['name'] + '\r\n' + form.cleaned_data['phone'] + '\r\n' + '\r\n'
                message += form.cleaned_data['brand'] + ' ' + form.cleaned_data['model'] + '\r\n' + '\r\n'
                message += form.cleaned_data['serv']
                
                to_email = ['alexthemaggot23@gmail.com', ]

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                return redirect('/')
        return redirect('/wrong')