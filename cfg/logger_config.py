import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
LOGGERS_LOG_LEVEL = 'WARNING'  # 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'
HANDLERS_LOG_LEVEL = 'WARNING'  # 'INFO', 'DEBUG', 'WARNING', 'ERROR', 'CRITICAL'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s | [%(levelname)s] | in module: %(module)s | %(filename)s:%(lineno)s | %(message)s'
        }
    },
    'handlers': {
        'std': {
            'level': f'{HANDLERS_LOG_LEVEL}',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': f'{HANDLERS_LOG_LEVEL}',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 104857600,
            'backupCount': 3,
            'formatter': 'standard',
            'filename': f'{BASE_DIR}/logs/logs.log',
        }
    },
    'loggers': {
        'logger': {
            'handlers': ['std', 'file'],
            'level': f'{LOGGERS_LOG_LEVEL}',
            'propagate': False
        },
    }
}
