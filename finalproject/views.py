from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.urls import path
from django.conf import settings
from pathlib import Path
from finalproject import settings


def index(request):
    return render(request, 'index.html', {'hello': 'this is from django backend'})

def djangocontent(request):
    return render(request, 'index.html', {'djangoboy': 'this is dynamically from django!'})


# for email sending
def base(request):
    # form_data = request.session.get('form_data')
    # context = {'form_data':form_data}
    send_mail('This is a test email',
              "This is to test if email body is being send correctly!",
              'Faizan.AIedu@gmail.com',
              ['faizan.kalkoti@gmail.com'],
              fail_silently = False)
    dict = {'email': 'email has been sent!'}
    return render(request, 'index.html', dict)



def send_with_attachment(request):
    mail = EmailMessage("subject", "message", "Faizan.AIedu@gmail.com", ['yohamchiki@gmail.com'])
    image_path = Path.joinpath(settings.BASE_DIR, 'static/accounts/photos/login-books.png')
    mail.attach_file(image_path)
    mail.send()
    d ={"attachment":"attachment sent successfully!"}
    return render(request, 'index.html', d)