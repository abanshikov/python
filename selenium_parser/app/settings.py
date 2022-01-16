import logging.config
import os
from pathlib import Path

# files and directory settings
path = Path(os.getcwd())
parent_path = str(path.parent)
PATH_CSV = parent_path + '/data/csv/'
PATH_DB = parent_path + '/data/db/'
PATH_IMG = parent_path + '/data/img/'
PATH_JSON = parent_path + '/data/json/'
PATH_LOG = parent_path + '/data/log/'
PATH_XLS = parent_path + '/data/xls/'
FILE_LOG = PATH_LOG + 'protocol.log'

# login settings
logging.getLogger('urllib3').setLevel('CRITICAL')
LEVEL_FILE = 'WARNING'
LEVEL_CONSOLE = 'DEBUG'
logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file_format': {
            'format': '{levelname}: \t{asctime} {filename} {funcName}(): '
                      '#{lineno}\t{message}',
            'style': '{',
        },
        'console_format': {
            'format': '%(levelname)s: \t%(asctime)s.%(msecs)03d %(filename)s '
                      '%(funcName)s(): #%(lineno)s\t%(message)s',
            'datefmt': '%H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': LEVEL_FILE,
            'filename': FILE_LOG,
            'mode': 'w',
            'formatter': 'file_format',
        },
        'console': {
            'class': 'logging.StreamHandler',
            'level': LEVEL_CONSOLE,
            'formatter': 'console_format',
        },
    },
    'loggers': {
        'log': {
            'level': 'DEBUG',
            'handlers': ['file', 'console'],
            'propagate': False,
        }
    },
    'filters': {},
    'root': {},
}
logging.config.dictConfig(logger_config)
log = logging.getLogger('log')
