import os
import smtplib

from dotenv import load_dotenv
from email.mime.text import MIMEText

import consts as c

from logic.logger import logger as lg


class MailHandler:
    """
    Класс для обработки и отправки электронных писем.

    Methods
    -------
    - prepare_message(data)
        Подготавливает сообщение для отправки по электронной почте.

    - send_email(to, subject, msg)
        Отправляет электронное письмо.
    """

    def __init__(self) -> None:
        load_dotenv()

        self.smtp_server: str = os.getenv(c.SMTP_SERVER_KEY)
        self.smtp_port: int = os.getenv(c.SMTP_PORT_KEY)
        self.sender: str = os.getenv(c.SENDER_ADDRESS_KEY)
        self.password: str = os.getenv(c.EMAIL_PASSWORD_KEY)

    def prepare_message(self, data: dict[str, list[dict[str, str]]]) -> str:
        """
        Подготавливает сообщение для отправки по электронной почте.

        Parameters
        ----------
        - data: dict
            Словарь с данными о просроченных документах для вставки этих данных
            в сообщение.

        Returns
        -------
        - message: str
            Подготовленное сообщение для отправки по электронной почте.
        """

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

    def send_email(self, to: str, subject: str, msg: str) -> None:
        """
        Отправляет электронное письмо. Если включена симуляция, то
        отправка не происходит, а просто выводится сообщение об успешной
        отправке в логи. Если выключен продакшн, то используется адрес
        электронной почты, указанный в переменной окружения вместо адреса
        получателя.

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
                return
        else:
            lg.info("Simulate mail sending is on.")
            lg.info("Consider the email sent successfully.")
