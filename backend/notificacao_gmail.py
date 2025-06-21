
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv
from .notificacao import Notificacao

class Notificacao_Email(Notificacao):
    def __init__(self, email):
        super().__init__(email)
    def manda_notificacao(self):
        load_dotenv()

        SENDER_EMAIL = os.getenv('MEU_EMAIL_REMETENTE')
        SENDER_PASSWORD = os.getenv('MINHA_SENHA_APP')

        RECEIVER_EMAIL = self.email
        SUBJECT = 'Notificacao do Meu Programa Python'

        BODY_HTML = """
        <html>
        <body>
            <h2>Ola!</h2>
            <p>Esta e uma notificacao simples enviada de Achados e Latidos Python.</p>
            <p>Seu email foi cadastrado em nosso site, se não foi você que fez isso entre em contato com a operadora do seu e-mail.</p>
            <p>Atenciosamente,<br>Achados e Latidos</p>
        </body>
        </html>
        """

        msg = MIMEMultipart('alternative')
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = SUBJECT

        msg.attach(MIMEText(BODY_HTML, 'html'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
            #print(f"E-mail enviado com sucesso para {RECEIVER_EMAIL}!")

        except Exception as e:
            print(f"Ocorreu um erro ao enviar o e-mail: {e}")
        finally:
            if 'server' in locals() and server:
                server.quit()

