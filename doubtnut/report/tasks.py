from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from fpdf import FPDF

pdf = FPDF()

from doubtnut import utils


@shared_task
def send_mail(data, user_email):

    print (data)

    print ("--------start--------")

    pdf.add_page()
    pdf.set_font('Arial', '', 14)  
    pdf.ln(10)
    pdf.write(5, data)
    # pdf.image("/home/shivam/Pictures/profile.png", 50, 50)
    pdf.output('sample.pdf', 'F')
    print ("-------end----------")

    send_mail(
            subject='Questions List',
            message=render_to_string('questions_list.txt'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user_email],
            html_message=render_to_string('questions_list.html'),
            fail_silently=False,
        )
