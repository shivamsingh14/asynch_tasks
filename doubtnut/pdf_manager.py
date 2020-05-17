import os
from doubtnut.app_logger import AppLogger

from django.conf import settings
from fpdf import FPDF

logger = AppLogger('CSV Manager')

class PdfManager():
    
    def __init__(self, filename, font, font_size, data):

        self.filename = filename 

        output_path = os.path.join(settings.MEDIA_ROOT, "reports/")

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        self.filepath = output_path + self.filename + '.pdf'

        self.font = font
        self.font_size = font_size
        self.data = data

        logger.info("Filepath: %s" % self.filepath)

    def generate_pdf(self):

        pdf = FPDF()

        logger.info("generate pdf Filepath: {}".format(self.filepath))
        logger.info("generate pdf font: {}".format(self.font))
        logger.info("generate pdf font size: {}".format(self.font_size))
        logger.info("Data in pdf: {}".format(self.data))

        logger.info ("--------start--------")
        pdf.add_page()
        pdf.set_font(self.font, '', self.font_size)  
        pdf.ln(10)
        pdf.write(5, self.data)
        pdf.output(self.filepath, 'F')
        logger.info ("-------end----------")
