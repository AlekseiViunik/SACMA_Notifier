from logic.json_handler import JsonHandler
from logic.excel_handler import ExcelHandler
from logic.logger import logger as lg
from logic.mail_handler import MailHandler
import consts as c


class Checker:
    """
    Основной класс для проверки файла Excel на наличие просроченных дат.

    Methods
    -------
    - check()
        Основной метод для проверки файла Excel на наличие просроченных дат.
    """

    def __init__(self) -> None:
        self.json: JsonHandler = JsonHandler(c.SETTINGS_JSON_ABS)
        self.excel: ExcelHandler = ExcelHandler()
        self.excel_filepath: str = c.EMPTY_STRING

    def check(self) -> None:
        """
        Основной метод для проверки файла Excel на наличие просроченных дат.
        Запускет проверку экселя через метод check_file класса ExcelHandler.
        Если в файле найдены просроченные даты, отправляет уведомление
        ответственным работникам с помощью класса MailHandler.
        """

        lg.info("Start checking...")
        lg.info("Get excel file path from settings json file.")

        try:
            self.excel_filepath = self.json.get_value_by_key(
                c.EXCEL_FILEPATH_KEY
            )
            lg.info(f"Excel file path: {self.excel_filepath}")

        except KeyError as e:
            lg.error(f"Key not found in JSON file: {e}.")
            return
        except Exception as e:
            lg.error(f"An error occurred: {e}.")
            return

        self.excel.filepath = self.excel_filepath

        lg.info("Get the necessary info about responsible workers.")
        try:
            workers_info = self.json.get_value_by_key(c.WORKERS)
            workers = [item for item in workers_info.keys()]
            lg.info(f"Success! Responsible workers: {workers}.")
        except KeyError as e:
            lg.error(f"Key '{c.WORKERS}' not found in JSON file: {e}.")
            return
        except Exception as e:
            lg.error(f"An error occurred: {e}.")
            return

        result = {}
        for worker, info in workers_info.items():
            lg.info(
                f"+++++++=======Check information for {worker}.=======+++++++"
            )
            result[worker] = self.excel.check_file(
                info[c.START_COLUMN],
                info[c.END_COLUMN]
            )
        lg.info("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        lg.info("Finished checking the file for all responsible workers.")
        lg.info("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")

        if result:
            lg.info("There are expired dates!")

            # name - имя ответственного работника
            # data - Словарь с просрочкой по датам для этого работника
            for name, data in result.items():
                lg.info(
                    f"+++++++=======Prepare data for {name}.=======+++++++"
                )
                if not data:
                    lg.info(f"No expired dates for {name}.")
                    continue

                mailer = MailHandler()

                recipient = workers_info[name][c.EMAIL]
                lg.info(f"Set {name}'s email as '{recipient}'.")
                lg.info(f"Prepare message for {name}.")
                message = mailer.prepare_message(data)
                mailer.send_email(
                    recipient,
                    "Documenti in scadenza",
                    message
                )
        else:
            lg.info("No expired dates found.")
            return
