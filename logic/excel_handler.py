from openpyxl import load_workbook
from openpyxl.utils import column_index_from_string
from datetime import datetime, timedelta

import consts as c


class ExcelHandler:
    def __init__(self):
        self.filepath: str = c.EMPTY_STRING

    def check_file(
        self,
        start_col: str,
        end_col: str
    ) -> dict[str, list[dict[str, str]]]:
        wb = load_workbook(self.filepath, data_only=True)
        ws = wb[c.EXCEL_SHEET_NAME]
        result = {}
        today = datetime.today()
        threshold = today + timedelta(days=c.TIME_TRESHOLD)

        name_col = c.EXCEL_NAME_COL
        start_idx = column_index_from_string(start_col)
        end_idx = column_index_from_string(end_col)

        for row in ws.iter_rows(
            min_row=c.EXCEL_START_ROW,
            min_col=start_idx,
            max_col=end_idx
        ):
            row_index = row[0].row
            name = ws.cell(row=row_index, column=name_col).value
            if not name:
                continue

            row_result = []
            for idx, cell in enumerate(row, start=start_idx):
                if isinstance(cell.value, datetime):
                    if cell.value <= threshold:
                        header = ws.cell(row=c.HEADER_ROW, column=idx).value
                        row_result.append(
                            {header: cell.value.strftime("%Y-%m-%d")}
                        )

            if row_result:
                result[name] = row_result

        wb.close()
        return result
