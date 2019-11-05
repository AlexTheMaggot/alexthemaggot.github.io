from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail

from .forms import ReviewForm

class ReviewView(View):

    def post(self, request):
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                form.save()

                subject = 'Новый отзыв на сайте'
                from_email = 'alex23_95@mail.ru'
                message = 'На сайте оставлен новый отзыв'

                to_email = ['alexthemaggot23@gmail.com', ]

                send_mail(subject, message, from_email, to_email, fail_silently=False)
                return redirect('/reviews')
        return redirect('/wrong')