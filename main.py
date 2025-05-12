import os


from logic.checker import Checker
from logic.logger import logger as lg
import consts as c

if __name__ == "__main__":

    def check_log_size() -> None:
        """
        Проверяет размер файла лога. Если он превышает MAX_LOG_LINES
        (20000 строк по умолчанию), очищает его.
        """

        if os.path.exists(c.LOG_PATH):
            with open(c.LOG_PATH, "r", encoding="utf-8") as f:
                lines = f.readlines()
            if len(lines) > c.MAX_LOG_LINES:
                with open(c.LOG_PATH, "w", encoding="utf-8"):
                    pass  # очищаем

    check_log_size()

    lg.info("================================================================")
    lg.info("Starting the script...")
    checker = Checker()
    checker.check()
    lg.info("Script finished.")
    lg.info("================================================================")
