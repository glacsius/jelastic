import os
import mimetypes
import smtplib
from email import encoders
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
from datetime import datetime


class Email(object):

    def _adiciona_anexo(self, msg, filename):
        if not os.path.isfile(filename):
            return
        ctype, encoding = mimetypes.guess_type(filename)
        if ctype is None or encoding is not None:
            ctype = 'application/octet-stream'

        maintype, subtype = ctype.split('/', 1)

        if subtype == 'xml':  # isso aqui é necessário por causa q gmail e outlook, se text, alteram o arquivo
            maintype = 'application'

        if maintype == 'text':
            with open(filename) as f:
                mime = MIMEText(f.read(), _subtype=subtype)
        elif maintype == 'image':
            with open(filename, 'rb') as f:
                mime = MIMEImage(f.read(), _subtype=subtype)
        elif maintype == 'audio':
            with open(filename, 'rb') as f:
                mime = MIMEAudio(f.read(), _subtype=subtype)
        else:
            with open(filename, 'rb') as f:
                mime = MIMEBase(maintype, subtype)
                mime.set_payload(f.read())

            encoders.encode_base64(mime)
        mime.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filename))
        msg.attach(mime)

    def enviar_email(self, de, para, assunto, corpo, anexos=None):
        # back a funciona no desespero
        smtp_host, smtp_porta = 'mail.akssistemas.com.br', '587'
        smtp_user, smtp_pass = 'suporte@akssistemas.com.br', '152634789'

        # smtp_host, smtp_porta = 'smtp.sparkpostmail.com', 587
        # smtp_user, smtp_pass = 'SMTP_Injection', '6b3e65c0c45958538dd875a86f4f0c43688718f6'
        de = 'nfe@notas.akssistemas.com.br'

        if type(para) == str:
            para = [para]
        msg = MIMEMultipart()
        msg['From'] = de
        msg['To'] = ', '.join(para)
        msg['Subject'] = assunto
        msg.attach(MIMEText(corpo, 'html', 'utf-8'))
        if anexos:
            for anexo in anexos:
                self._adiciona_anexo(msg, anexo)
        raw = msg.as_string()
        # smtp = smtplib.SMTP_SSL(host=smtp_host, port=smtp_porta)
        smtp = smtplib.SMTP(host=smtp_host, port=smtp_porta)
        # se precisa do tls tem q usar o  smtplib.SMTP e depois chamar o
        # smtp.starttls()
        # smtp.ehlo()
        try:
            try:
                smtp.login(smtp_user, smtp_pass)
                smtp.sendmail(de, para, raw)
                return False
            except Exception as e:
                return "ERRO AO ENVIAR EMAIL: "+str(e)
        finally:
            smtp.quit()
