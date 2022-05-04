import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s | [%(levelname)s] | in method: %(funcName)s | %(filename)s:%(lineno)s | %(message)s'
        }
    },
    'handlers': {
        'std': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
        'file': {
            'level': 'DEBUG',
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
            'level': 'WARNING',
            'propagate': False
        },
    }
}
