"""
Here the principal consts are defined.
"""

PRODUCTION_MODE = False
SIMULATE_MAIL_SENDING = True


EXE_FROZEN = 'frozen'

EMPTY_STRING = ''

STR_CODING = 'utf-8'
FILE_READ = 'r'
FILE_WRITE = 'w'

FNF_MESSAGE = 'File not found.'
INDENT = 4
SET_TO_ZERO = 0
SET_TO_ONE = 1

SETTINGS_JSON_ABS = "settings.json"

# Excel consts
if True:
    EXCEL_FILEPATH_KEY = "filepath"
    EXCEL_SHEET_NAME = "Foglio1"
    EXCEL_START_ROW = 4
    EXCEL_NAME_COL = 2
    EXCEL_END_COL = 7
    HEADER_ROW = 3

TIME_TRESHOLD = 30

# Dict keys
if True:
    WORKERS = "workers"
    EMAIL = "email"
    START_COLUMN = "start_column"
    END_COLUMN = "end_column"

# ENV keys
if True:
    SMTP_SERVER_KEY = "SMTP_SERVER"
    SMTP_PORT_KEY = "SMTP_PORT"
    SENDER_ADDRESS_KEY = "EMAIL_ADDRESS"
    EMAIL_PASSWORD_KEY = "EMAIL_PASSWORD"
    RECIPIENT_KEY = "DEFAULT_RECIPIENT"

# Mail consts
if True:
    SUBJECT = "Subject"
    FROM = "From"
    TO = "To"

# Logger consts
if True:
    LOG_DIR = "logs"
    LOG_FILE = "app.log"
    LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    LOG_DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
    LOG_LEVEL = "INFO"
    LOG_ENCODING = "utf-8"
