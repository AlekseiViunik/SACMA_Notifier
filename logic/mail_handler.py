import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText

import consts as c

from logic.logger import logger as lg


class MailHandler:
    def __init__(self):
        load_dotenv()

        self.smtp_server: str = os.getenv(c.SMTP_SERVER_KEY)
        self.smtp_port: int = os.getenv(c.SMTP_PORT_KEY)
        self.sender: str = os.getenv(c.SENDER_ADDRESS_KEY)
        self.password: str = os.getenv(c.EMAIL_PASSWORD_KEY)

    def prepare_message(self, data):
        message = (
            "I seguenti documenti sono prossimi alla scadenza o sono già "
            "scaduti:\n"
        )
        for name, info in data.items():
            message += f"• Per {name}:\n"
            for info_item in info:
                for key, value in info_item.items():
                    message += f"\t•• '{key}' scade il '{value}';\n"

        return message

    def send_email(self, to: str, subject: str, msg: str):
        """
        Отправляет электронное письмо.

        Parameters
        ----------
        - to: str
            Адрес электронной почты получателя.

        - subject: str
            Тема письма.

        - msg: str
            Текст сообщения.
        """

        if not c.PRODUCTION_MODE:
            lg.info("Production mode is off. Using default recipient.")
            to = os.getenv(c.RECIPIENT_KEY)

        lg.info("Set up email message.")
        mime_msg = MIMEText(msg)
        mime_msg[c.SUBJECT] = subject
        mime_msg[c.FROM] = self.sender
        mime_msg[c.TO] = to

        if not c.SIMULATE_MAIL_SENDING:
            lg.info(f"Trying to send email to '{to}' from '{self.sender}'.")
            try:
                with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                    server.starttls()
                    server.login(self.sender, self.password)
                    server.send_message(mime_msg)
                    lg.info("Email sent successfully!")

            except Exception as e:
                lg.error(f"Error sending email: {e}")
                print(f"Error sending email: {e}")
        else:
            lg.info("Simulate mail sending is on.")
            lg.info("Consider the email sent successfully.")
