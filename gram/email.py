from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def welcome_email(name,receiver):
    subject = 'Welcome to @Moments'
    sender = 'nzauprojects@gmail.com'

    text_content = render_to_string('email/welcome_email.txt',{'name':name})
    html_content = render_to_string('email/welcome_email.html',{'name':name})

    message = EmailMultiAlternatives(subject,text_content,sender.[receiver])
    message.attach_alternative(html_content,'text/html')
    message.send()