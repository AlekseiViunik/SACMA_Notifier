from logic.json_handler import JsonHandler
from logic.excel_handler import ExcelHandler
from logic.mail_handler import MailHandler
import consts as c


class Checker:
    def __init__(self):
        self.json: JsonHandler = JsonHandler(c.SETTINGS_JSON_ABS)
        self.excel: ExcelHandler = ExcelHandler()
        self.excel_filepath: str = c.EMPTY_STRING

    def check(self):
        self.excel_filepath = self.json.get_value_by_key(c.EXCEL_FILEPATH_KEY)
        self.excel.filepath = self.excel_filepath

        workers_info = self.json.get_value_by_key(c.WORKERS)

        result = {}
        for worker, info in workers_info.items():

            result[worker] = self.excel.check_file(
                info[c.START_COLUMN],
                info[c.END_COLUMN]
            )

        if result:
            for name, data in result.items():
                if not data:
                    continue
                mailer = MailHandler()
                recipient = workers_info[name][c.EMAIL]
                message = mailer.prepare_message(data)
                mailer.send_email(
                    recipient,
                    "Documenti in scadenza",
                    message
                )
        else:
            print("No results found.")
