from openpyxl import load_workbook
from datetime import datetime, timedelta
import consts as c


class ExcelHandler:
    def __init__(self):
        self.filepath: str = c.EMPTY_STRING

    def check_file(self) -> dict[str, list[str]]:
        wb = load_workbook(self.filepath, data_only=True)
        ws = wb[c.EXCEL_SHEET_NAME]
        result = {}
        today = datetime.today()
        threshold = today + timedelta(days=c.TIME_TRESHOLD)

        for row in ws.iter_rows(
            min_row=c.EXCEL_START_ROW,
            min_col=c.EXCEL_START_COL,
            max_col=c.EXCEL_END_COL
        ):
            name_cell = row[c.SET_TO_ZERO]
            name = name_cell.value
            if not name:
                continue

            near_expiry = []
            for cell in row[c.SET_TO_ONE:]:
                if isinstance(cell.value, datetime):
                    if today <= cell.value <= threshold:
                        near_expiry.append(cell.coordinate)

            if near_expiry:
                result[name] = near_expiry

        wb.close()
        return result
