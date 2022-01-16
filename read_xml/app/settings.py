import logging.config
import os

# files
CWD = os.getcwd()
os.chdir(os.path.join(os.path.dirname(__file__), os.pardir))
DATA = os.getcwd() + '/data/'
DIR_XML = DATA + 'xml/'
DIR_LOG = DATA + 'log/'
FILE_LOG = DIR_LOG + 'protocol.log'

# log setting
LEVEL_FILE = 'DEBUG'
LEVEL_CONSOLE = 'INFO'
logger_config = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'file_format': {
            'format': '{levelname}: {asctime} {funcName}(): #{lineno}\t{message}',
            'style': '{',
        },
        'console_format': {
            'format': '%(levelname)s: \t%(asctime)s.%(msecs)03d %(funcName)s(): #%(lineno)s\t%(message)s',
            'datefmt': '%H:%M:%S',
        }
    },
    'handlers': {
        'file': {
            'class': 'logging.FileHandler',
            'level': LEVEL_FILE,
            'filename': FILE_LOG,
            'mode': 'a',
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
