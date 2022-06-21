import os
import logging.config

from dotenv import load_dotenv

from cfg.logger_config import LOGGING

# load env variables
load_dotenv()

# logger init
logging.config.dictConfig(LOGGING)
logger = logging.getLogger('logger')


# Timeouts
SMALL_TIMEOUT = 5
TIMEOUT = 10
LARGE_TIMEOUT = 20


# URLs
TEXT_BOX_URL = 'https://demoqa.com/text-box'
CHECK_BOX_URL = 'https://demoqa.com/checkbox'
LOGIN_URL = 'https://demoqa.com/login'
RADIO_BUTTON_URL = 'https://demoqa.com/radio-button'
WEB_TABLES_URL = 'https://demoqa.com/webtables'
BUTTONS_URL = 'https://demoqa.com/buttons'
LINKS_URL = 'https://demoqa.com/links'

USER_NAME = os.getenv('USER_NAME')
PASSWORD = os.getenv('PASSWORD')

