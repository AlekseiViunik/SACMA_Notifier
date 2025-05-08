from logic.json_handler import JsonHandler
from logic.excel_handler import ExcelHandler
import consts as c


class Checker:
    def __init__(self):
        self.json: JsonHandler = JsonHandler(c.SETTINGS_JSON_ABS)
        self.excel: ExcelHandler = ExcelHandler()
        self.excel_filepath: str = c.EMPTY_STRING

    def check(self):
        self.excel_filepath = self.json.get_value_by_key(c.EXCEL_FILEPATH_KEY)
        self.excel.filepath = self.excel_filepath
        self.excel.check_file()
