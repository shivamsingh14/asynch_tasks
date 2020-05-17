from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from doubtnut.app_logger import AppLogger
from doubtnut.email_sender import EmailSender
from doubtnut.pdf_manager import PdfManager

import os, uuid

logger = AppLogger(tag="Tasks")

from doubtnut import utils


@shared_task
def send_mail_task(data, user_email):

    logger.info("Data: {}. User email id: {}".format(data, user_email))

    unique_key = uuid.uuid4()
    filename = "report - {}".format(str(unique_key))
    pdf_manager = PdfManager(filename=filename, font="Arial", font_size=14, data=data)
    pdf_manager.generate_pdf()
    filepath = pdf_manager.filepath
    logger.info("Filepath: {}".format(filepath))

    subject = 'Last Interaction Questions'
    email_to = [user_email]
    attachments = [filepath,]
    text_content = render_to_string('questions_list.txt')
    html_content = render_to_string('questions_list.html')
    email_sender = EmailSender(subject=subject, text_content=text_content, html_content=html_content,
                        to=email_to, attachments=attachments)
    logger.info("Sending email")
    email_sender.send()
    logger.info("Mail Sent Successfully")

