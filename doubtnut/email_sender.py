from django.core.mail import EmailMultiAlternatives, get_connection
from django.conf import settings

from doubtnut.app_logger import AppLogger

logger = AppLogger(tag="Email Sender")

class EmailSender(object):

	def __init__(self, subject, text_content, html_content, attachments=[], to=[], cc=[], bcc=[]):
		self.subject = subject
		self.text_content = text_content
		self.html_content = html_content
		self.attachments = attachments
		self.to = to
		self.cc = cc
		self.bcc = bcc
		

		logger.info("Subject: %s" % self.subject)
		logger.info("TO: %s" % self.to)
		logger.info("CC: %s" % self.cc)
		logger.info("BCC: %s" % self.bcc)
		logger.info("Attachments: %s" % self.attachments)
		logger.info("Text content: %s" % self.text_content)

	def send(self, from_email=settings.EMAIL_HOST_USER, password=settings.EMAIL_HOST_PASSWORD):

		logger.info("Creating connection")
		logger.info("Username: {}, password: {}".format(from_email, password))

		connection = get_connection(username=from_email,
									password=password,
									fail_silently=False)

		logger.info("Connection made, connection: {}".format(connection))

		message = EmailMultiAlternatives(self.subject, self.text_content,
							to=self.to, cc=self.cc, bcc=self.bcc, 
							from_email=from_email, 
							connection=connection)

		logger.info("Message: {}".format(message))

		message.attach_alternative(self.html_content, "text/html")

		for attachment in self.attachments:
			message.attach_file(attachment)

		logger.info("Message: {}".format(message))

		message.send()